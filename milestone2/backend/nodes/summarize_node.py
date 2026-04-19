import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def summarize_node(state):
    documents = state.get('documents', [])
    print(f"--- SUMMARIZING: {len(documents)} Documents ---")
    
    llm = ChatOpenAI(model="gpt-3.5-turbo") # Or use Groq model name
    
    summaries = []
    for doc in documents:
        prompt = f"Summarize the following research content from {doc['url']}:\n\n{doc['content'][:5000]}"
        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            summaries.append(response.content)
        except Exception as e:
            print(f"Error summarizing {doc['url']}: {e}")
            
    return {"summaries": summaries}
