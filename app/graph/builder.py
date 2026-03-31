from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes import (
    segregator_node,
    id_node,
    discharge_node,
    bill_node,
    aggregator_node
)

builder = StateGraph(GraphState)

builder.add_node("segregator", segregator_node)
builder.add_node("id_agent", id_node)
builder.add_node("discharge_agent", discharge_node)
builder.add_node("bill_agent", bill_node)
builder.add_node("aggregator", aggregator_node)

builder.set_entry_point("segregator")

builder.add_edge("segregator", "id_agent")
builder.add_edge("segregator", "discharge_agent")
builder.add_edge("segregator", "bill_agent")

builder.add_edge("id_agent", "aggregator")
builder.add_edge("discharge_agent", "aggregator")
builder.add_edge("bill_agent", "aggregator")

builder.add_edge("aggregator", END)

graph = builder.compile()