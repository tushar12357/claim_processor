from app.core.llm import call_llm, safe_parse

def extract_bill(text):
    prompt = f"""
Return ONLY JSON.

Extract:
- items (list with name and cost)
- total_amount

Text:
{text}
"""
    return safe_parse(call_llm(prompt))