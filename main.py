from dotenv import load_dotenv
from linkedin_agent import LinkedInPostGenerator


def save_post_to_file(post: str, language: str) -> str:
    safe_lang = language.strip().lower().replace(" ", "_") or "output"
    output_path = f"linkedin_post_{safe_lang}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(post)
    return output_path


def save_post_to_html(post: str, language: str) -> str:
    
        safe_lang = language.strip().lower().replace(" ", "_") or "output"
        output_path = f"linkedin_post_{safe_lang}.html"
        paragraphs = [p.strip() for p in post.split("\n\n") if p.strip()]
        body = "\n".join(f"<p>{p}</p>" for p in paragraphs)

        html = f"""<!doctype html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Generated LinkedIn Post</title>
    <style>
        :root {{
            color-scheme: light;
        }}
        body {{
            margin: 0;
            padding: 32px;
            font-size: 20px;
            line-height: 1.8;
            color: #111827;
            background: #f7f7f8;
            font-family: "Noto Sans Bengali", "Hind Siliguri", "SolaimanLipi", "Kalpurush", sans-serif;
        }}
        main {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            padding: 24px;
        }}
        p {{ margin: 0 0 16px 0; }}
    </style>
</head>
<body>
    <main>
        <h2>Generated LinkedIn Post ({language})</h2>
        {body}
    </main>
</body>
</html>
"""

        with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)
        return output_path

def main():
    # Step 1: Load API key.
    load_dotenv()

    # Step 2: Init the AI Agent
    print("\n LinkedIn Post Generator  ")
    agent = LinkedInPostGenerator()
    
    # Step 3: Get user input

    topic = input("Enter post topic: ").strip()
    language = input("Enter language (e.g., English, Bengali, Spanish): ").strip()
    
    # Step 4: Generate the post
    
    print("\nGenerating post...\n")
    try:
        post = agent.generate_post(topic, language)
    except Exception as error:
        print("Failed to generate post:")
        print(str(error))
        return
    
    # Step 5: Output the result
    print("=" * 60)
    print("YOUR LINKEDIN POST:\n")
    print(post)
    print("=" * 60)

    text_file_path = save_post_to_file(post, language)
    html_file_path = save_post_to_html(post, language)
    print(f"Saved UTF-8 text output to: {text_file_path}")
    print(f"Saved browser-friendly output to: {html_file_path}")

if __name__ == "__main__":
    main()
