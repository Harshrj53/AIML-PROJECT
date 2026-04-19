import os
from tavily import TavilyClient

def search_node(state):
    query = state.get('query')
    print(f"--- SEARCHING: {query} ---")
    
    tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
    response = tavily.search(query=query, search_depth="advanced", max_results=5)
    
    urls = [result['url'] for result in response['results']]
    return {"urls": urls}
