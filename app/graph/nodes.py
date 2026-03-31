from app.agents.segregator import classify_pages
from app.agents.id_agent import extract_id
from app.agents.discharge_agent import extract_discharge
from app.agents.bill_agent import extract_bill
from app.services.parser import join_pages


def segregator_node(state):
    classified = classify_pages(state["pages"])
    return {"classified_pages": classified}


def id_node(state):
    indices = state["classified_pages"].get("identity_document", [])
    text = join_pages(state["pages"], indices)
    return {"id_data": extract_id(text)}


def discharge_node(state):
    indices = state["classified_pages"].get("discharge_summary", [])
    text = join_pages(state["pages"], indices)
    return {"discharge_data": extract_discharge(text)}


def bill_node(state):
    indices = state["classified_pages"].get("itemized_bill", [])
    text = join_pages(state["pages"], indices)
    return {"bill_data": extract_bill(text)}


def aggregator_node(state):
    return {
        "final_output": {
            "identity": state.get("id_data", {}),
            "discharge": state.get("discharge_data", {}),
            "billing": state.get("bill_data", {})
        }
    }