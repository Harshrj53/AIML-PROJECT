import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import json

def report_node(state):
    insights = state.get('insights', "")
    validated = state.get('validated', "")
    urls = state.get('urls', [])
    query = state.get('query', "")
    
    print(f"--- GENERATING FINAL REPORT ---")
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    prompt = (
        "Generate a structured research report based on the following insights and validation results. "
        "The response MUST be in JSON format with the following keys: 'title', 'abstract', 'key_findings', 'conclusion'.\n\n"
        f"Query: {query}\n"
        f"Insights: {insights}\n"
        f"Validation: {validated}"
    )
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        # Strip potential markdown formatting if LLM returns it
        content = response.content.replace("```json", "").replace("```", "").strip()
        report_json = json.loads(content)
        report_json['sources'] = urls
    except Exception as e:
        print(f"Error in report node: {e}")
        report_json = {
            "title": f"Research Report: {query}",
            "abstract": "Summary could not be generated.",
            "key_findings": insights,
            "conclusion": "Final conclusion pending.",
            "sources": urls
        }
        
    return {"report": report_json}
