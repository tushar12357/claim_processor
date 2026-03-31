from app.core.llm import call_llm, safe_parse

def classify_pages(pages):
    prompt = f"""
Return ONLY valid JSON.

Classify each page into ONE of these types:
claim_forms, cheque_or_bank_details, identity_document,
itemized_bill, discharge_summary, prescription,
investigation_report, cash_receipt, other

Return format:
{{
  "identity_document": [0,2],
  "discharge_summary": [1],
  "itemized_bill": [3]
}}

Pages:
{pages}
"""

    result = call_llm(prompt)
    return safe_parse(result)