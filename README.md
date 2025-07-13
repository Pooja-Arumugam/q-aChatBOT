# AI Text Generation App

A simple and interactive **Streamlit** app that lets you generate text using a language model. You can fine-tune the generation behavior with customizable **temperature** and **max token** settings, and securely input your **API key** for access.

---

## Features

- Secure API key input via sidebar
- Adjustable **Temperature** slider to control randomness
- Set **Maximum Token Limit** to define response length
- Powered by a language model (e.g., OpenAI, Groq, etc.)
- Lightweight and responsive UI with Streamlit

---

## What Motivated Me to Build This Project

As someone passionate about language models and user-friendly tools, I wanted to create a lightweight yet powerful interface that allows anyone to experiment with text generation in real time. Most LLM APIs are accessible only through code, so I built this app to make that experience interactive, visual, and beginner-friendly — no coding required.

This project is also a step toward democratizing AI tools and helping people understand how small changes (like temperature and token count) can dramatically impact AI behavior.

---

## Project Highlights: A Technical Overview

- **Framework**: Built using [Streamlit](https://streamlit.io/) for a fast, responsive, and clean UI.
- **API Integration**: Connects securely to an LLM backend (e.g., OpenAI, Groq) using a user-provided API key.
- **Dynamic Controls**: 
  - **Temperature Slider**: Controls response randomness (`0.0` = consistent, `1.0` = diverse).
  - **Max Tokens Slider**: Limits output length for precise control over verbosity.
- **Security**: API key input is session-based and never stored or logged.
- **Customization-Ready**: Easily extendable to support multiple models, prompt templates, or response formatting.

---

## Why This Matters to Me

Language models are powerful tools, but they’re often hidden behind developer interfaces. I believe that giving everyone — from students to creators — an intuitive way to interact with these models can unlock creativity, learning, and innovation. This app is my contribution to that goal: making cutting-edge AI more accessible and understandable for all.
---

## App Preview
<img width="1838" height="886" alt="image" src="https://github.com/user-attachments/assets/17ec611d-43d4-4bf3-9e3c-7587f2839bf6" />


---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-text-generator-app.git
cd ai-text-generator-app
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
```
#### On macOS/Linux:
```bash
source venv/bin/activate
```
#### On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

## How to Run the App
``` bash
streamlit run app.py
```
---

## Sidebar Controls Explained
### API Key Input
- Securely enter your private API key
- Used to authenticate with the LLM provider
- Not stored, shared, or logged

### Temperature
- Controls randomness of response generation
- 0.0 = deterministic (same result each time)
- 1.0 = creative and varied responses

## Max Tokens
- Sets the maximum length of the response
- Higher = longer, more detailed replies
- Example: 150 tokens ≈ 100–150 words

--- 
## Sample Prompts
- Try out:
Explain black holes like I'm 5 years old.
Write a haiku about autumn.
Summarize the movie Interstellar in 3 sentences.
Generate a business idea using AI.
---

## Requirements
- Python 3.7+
- streamlit
- requests
    python-dotenv (optional, for .env API key support)

## Security Notice
- API keys are entered securely in the sidebar
- They are used only during your session
- The app does not store or transmit your key

## Future Roadmap
 - Add support for multiple LLMs (OpenAI, Groq, Claude)
 - Save prompt history
 - Export responses to text/PDF
 - Prompt templates & presets



