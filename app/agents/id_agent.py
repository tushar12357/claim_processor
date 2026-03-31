from app.core.llm import call_llm, safe_parse

def extract_id(text):
    prompt = f"""
Return ONLY JSON.

Extract:
- patient_name
- dob
- policy_number
- id_number

Text:
{text}
"""
    return safe_parse(call_llm(prompt))