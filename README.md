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



