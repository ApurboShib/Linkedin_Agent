import os
import unicodedata
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class LinkedInPostGenerator:
   
    def __init__(self, model_name="gemini-2.5-flash", temperature=0.7):
        # Step 1: Securely load the API key from environment variable

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("key is missing! Please add it.")

        self.api_key = api_key
        self.temperature = temperature
        self.model_candidates = [
            model_name,
            "gemini-flash-latest",
            "gemini-2.5-flash",
            "gemini-2.0-flash",
        ]
        self.active_model = self.model_candidates[0]

        # Step 2: Init the LLM
        self.llm = self._build_llm(self.active_model)
        
        self._setup_chain()

    def _build_llm(self, model_name: str) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=self.temperature,
            google_api_key=self.api_key,
        )

    def _setup_model(self, model_name: str):
        self.active_model = model_name
        self.llm = self._build_llm(model_name)
        self._setup_chain()

    @staticmethod
    def _is_model_not_found(error: Exception) -> bool:
        msg = str(error)
        return "NOT_FOUND" in msg or "NOT FOUND" in msg or "is not found" in msg

    @staticmethod
    def _is_quota_error(error: Exception) -> bool:
        msg = str(error)
        return "RESOURCE_EXHAUSTED" in msg or "Quota exceeded" in msg

    def _setup_chain(self):
    
        # Step 3: Define Prompt 
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "You are a professional LinkedIn content creator. "
                "Write a post that is engaging, insightful, and structured in 2–4 short paragraphs. "
                "Use a conversational yet professional tone. "
                "Include a hook in the first sentence, add value in the middle, "
                "and end with a question or call to action (e.g., 'What’s your take?' or 'Share your experience below'). "
                "Avoid hashtags unless they are minimal and relevant."
            )),
            ("human", (
                "Topic: {topic}\n"
                "Language: {language}\n\n"
                "Language quality rule: {language_note}\n\n"
                "Generate a LinkedIn post following the guidelines above. "
                "Write entirely in {language}."
            ))
        ])
        
        # Step 4: Create the LCEL
        self.chain = self.prompt | self.llm | StrOutputParser()

    @staticmethod
    def _normalize_bengali_text(text: str) -> str:
        # Normalize Unicode and remove problematic invisible characters.
        cleaned = unicodedata.normalize("NFC", text)
        for ch in ("\u200b", "\ufeff"):
            cleaned = cleaned.replace(ch, "")
        cleaned = cleaned.replace("\r\n", "\n").replace("\r", "\n")
        return cleaned.strip()
    
    def generate_post(self, topic: str, language: str) -> str:

        language_lower = language.strip().lower()
        if language_lower in {"bangla", "bengali", "বাংলা", "বাঙলা"}:
            language_note = (
                "Write in clear, modern, easy-to-understand Bangla (বাংলা). "
                "Use everyday words, short sentences, and natural Bangladeshi/Indian Bangla style. "
                "Avoid overly literary, complex, or archaic vocabulary."
            )
            language = "বাংলা"
        else:
            language_note = (
                "Use clear, natural, easy-to-understand wording for native speakers "
                "of the requested language."
            )

        payload = {
            "topic": topic,
            "language": language,
            "language_note": language_note,
        }
        tried = []
        last_error = None

        for model in self.model_candidates:
            if model in tried:
                continue

            if model != self.active_model:
                self._setup_model(model)

            tried.append(model)
            try:
                response = self.chain.invoke(payload)
                post = response.strip()
                if language == "বাংলা":
                    post = self._normalize_bengali_text(post)
                return post
            except Exception as error:
                last_error = error
                if self._is_quota_error(error):
                    raise RuntimeError(
                        "Gemini API quota exceeded for this API key. "
                        "Please wait and retry, or enable billing in Google AI Studio / GCP."
                    ) from error
                if self._is_model_not_found(error):
                    continue

                raise

        raise RuntimeError(
            "No compatible Gemini model was available. "
            "Tried: " + ", ".join(tried)
        ) from last_error
