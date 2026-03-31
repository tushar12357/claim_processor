from app.graph.builder import graph


def test_graph_flow():
    state = {
        "pages": [
            "Patient Name: John Doe Aadhaar",
            "Diagnosis: Fever Discharge Summary",
            "Itemized Bill Total: 5000"
        ]
    }

    result = graph.invoke(state)

    assert "final_output" in result
    assert isinstance(result["final_output"], dict)