from typing import TypedDict, List, Dict, Any

class GraphState(TypedDict):
    pages: List[str]
    classified_pages: Dict[str, List[int]]
    id_data: Dict[str, Any]
    discharge_data: Dict[str, Any]
    bill_data: Dict[str, Any]
    final_output: Dict[str, Any]