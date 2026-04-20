from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from nodes.search_node import search_node
from nodes.retrieve_node import retrieve_node
from nodes.summarize_node import summarize_node
from nodes.reason_node import reason_node
from nodes.validate_node import validate_node
from nodes.report_node import report_node

class AgentState(TypedDict):
    query: str
    urls: List[str]
    documents: List[Dict[str, str]]
    summaries: List[str]
    insights: str
    validated: str
    report: Dict[str, Any]

def create_graph():
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("search", search_node)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("summarize", summarize_node)
    workflow.add_node("reason", reason_node)
    workflow.add_node("validate", validate_node)
    workflow.add_node("report", report_node)
    
    # Define Edges
    workflow.set_entry_point("search")
    workflow.add_edge("search", "retrieve")
    workflow.add_edge("retrieve", "summarize")
    workflow.add_edge("summarize", "reason")
    workflow.add_edge("reason", "validate")
    workflow.add_edge("validate", "report")
    workflow.add_edge("report", END)
    
    return workflow.compile()
