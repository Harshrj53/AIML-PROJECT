import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def reason_node(state):
    summaries = state.get('summaries', [])
    print(f"--- REASONING: Synthesizing {len(summaries)} summaries ---")
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    combined_summaries = "\n\n".join(summaries)
    prompt = f"Synthesize the following research summaries into key insights. Identify common themes, unique findings, and overall significance:\n\n{combined_summaries}"
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        insights = response.content
    except Exception as e:
        print(f"Error in reasoning node: {e}")
        insights = "No insights could be generated."
        
    return {"insights": insights}
