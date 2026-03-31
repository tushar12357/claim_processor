from app.core.llm import call_llm, safe_parse

def extract_discharge(text):
    prompt = f"""
Return ONLY JSON.

Extract:
- diagnosis
- admission_date
- discharge_date
- doctor_name

Text:
{text}
"""
    return safe_parse(call_llm(prompt))