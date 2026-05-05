#  LinkedIn AI Post Generator

A powerful, AI-driven tool designed to craft professional, engaging, and insightful LinkedIn posts in seconds. Built with **LangChain** and **Google Gemini**, this agent understands context, tone, and cultural nuances to help you build your professional brand effortlessly.

---

## Project Demo

Experience the agent in action! Watch how it generates high-quality content and provides a beautiful live preview.

<div align="center">
  <a href="Video/demo.mov">
    <img src="Video/thumbnail.png" alt="Watch Demo Video" width="100%">
  </a>
</div>

> [!TIP]
> **Click the image above to play the demo video.**

<div align="center">
  <video src="Video/demo.mov" width="100%" controls>
    <source src="Video/demo.mov" type="video/mp4">
    <source src="Video/demo.mov" type="video/quicktime">
    Your browser does not support the video tag.
  </video>
</div>

---

##  Key Features

- ** Intelligent Content Generation**: Uses Google's latest Gemini models to write structured, hook-driven LinkedIn posts.
- ** Multi-Language Support**: Generate posts in English, Bengali (বাংলা), Spanish, and more with native-level fluency.
- ** Live HTML Preview**: Automatically generates a sleek, premium HTML preview of your post that opens directly in your browser.
- ** Dual Export**: Saves your generated content in both `.txt` (raw text) and `.html` (styled preview) formats.
- ** Model Resilience**: Automatically falls back to alternative Gemini models if the primary one is unavailable.
- ** Bengali Optimization**: Specialized normalization for Bengali Unicode to ensure perfect rendering across all devices.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **LangChain**: For orchestration and LLM chaining.
- **Google Gemini API**: High-performance generative AI.
- **Vanilla CSS/HTML**: For the premium preview interface.
- **Dotenv**: Secure environment variable management.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python installed on your system.
- A Google AI Studio API Key. [Get one here](https://aistudio.google.com/).

### 2. Installation

Clone the repository and install the dependencies:

```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

##  How to Use

1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter your **Topic** (e.g., "The future of AI in coding").
3. Choose your **Language** (e.g., "English" or "Bengali").
4. Wait for the magic to happen! The post will be generated, saved, and opened in your browser automatically.

---

##  Project Structure

```text
.
├── Video/                  # Demo videos and media
│   └── demo.mov            # Project walk-through
├── main.py                 # Entry point & CLI logic
├── linkedin_agent.py       # AI Agent core logic & LangChain setup
├── requirements.txt        # Python dependencies
├── .env                    # Secret API keys (not in Git)
└── linkedin_post_*.html    # Generated post previews
```

---

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

---

<div align="center">
  <sub>Built by Joy Shib</sub>
</div>
