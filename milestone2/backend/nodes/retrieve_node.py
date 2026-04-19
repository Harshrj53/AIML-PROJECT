import requests
from bs4 import BeautifulSoup

def retrieve_node(state):
    urls = state.get('urls', [])
    print(f"--- RETRIEVING: {len(urls)} URLs ---")
    
    documents = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for element in soup(["script", "style"]):
                element.decompose()
            
            text = soup.get_text()
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            documents.append({"url": url, "content": text[:10000]}) # Limit content length
        except Exception as e:
            print(f"Error retrieving {url}: {e}")
            
    return {"documents": documents}
