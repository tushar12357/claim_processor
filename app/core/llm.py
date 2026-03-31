from groq import Groq
from app.core.config import GROQ_API_KEY
import json

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = "You are a precise JSON extraction assistant."

def call_llm(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content

def safe_parse(text: str):
    text = text.strip().replace("```json", "").replace("```", "")
    try:
        return json.loads(text)
    except:
        return {"raw": text}