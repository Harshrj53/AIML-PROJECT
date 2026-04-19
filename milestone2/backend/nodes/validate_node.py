import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def validate_node(state):
    insights = state.get('insights', "")
    print(f"--- VALIDATING INSIGHTS ---")
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    prompt = (
        "Analyze the following research insights for contradictions, uncertainties, or gaps in information. "
        "Provide a validation status (e.g., 'Validated' or 'Needs Review') and a brief explanation.\n\n"
        f"{insights}"
    )
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        validated = response.content
    except Exception as e:
        print(f"Error in validation node: {e}")
        validated = "Validation could not be completed."
        
    return {"validated": validated}
