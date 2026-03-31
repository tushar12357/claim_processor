from app.agents.segregator import classify_pages


def test_classify_pages():
    pages = [
        "Patient Name: John Doe Aadhaar",
        "Discharge Summary Diagnosis: Fever",
        "Itemized Bill Total: 5000"
    ]

    result = classify_pages(pages)

    assert isinstance(result, dict)