# ChatBot

A small Python chatbot project using the Groq (or Anthropic) API.

## Setup

1. Create a virtual environment and activate it:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requriments.txt
```

3. Create a `.env` file in the project root with your API keys (example):

```env
# Use the key your chosen SDK expects.
# For Groq:
GROQ_API_KEY=your_groq_key_here

# For Anthropic (if you switch to that):
ANTHROPIC_API_KEY=your_anthropic_key_here
```

4. Run the app:

```powershell
python .\app.py
```

## Notes

- Ensure `prompt.txt` exists in the same folder as `app.py`.
- `app.py` should load the prompt from `prompt.txt` and send it as the system message.
- If you get `model_not_found`, change the model name to one your key has access to.
