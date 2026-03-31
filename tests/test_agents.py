from app.agents.id_agent import extract_id
from app.agents.discharge_agent import extract_discharge
from app.agents.bill_agent import extract_bill


def test_id_agent():
    text = "Patient Name: John Doe DOB: 01-01-1990 Policy: ABC123"
    result = extract_id(text)

    assert isinstance(result, dict)


def test_discharge_agent():
    text = "Diagnosis: Fever Admission: 01-01-2024 Discharge: 05-01-2024 Doctor: Dr. Smith"
    result = extract_discharge(text)

    assert isinstance(result, dict)


def test_bill_agent():
    text = "Item: Medicine 2000, Room 3000 Total: 5000"
    result = extract_bill(text)

    assert isinstance(result, dict)