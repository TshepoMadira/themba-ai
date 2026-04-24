from ddgs import DDGS

def search_web(query: str) -> str:
    """Search the web using DuckDuckGo"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if not results:
                return "I couldn't find anything on that topic, sir."
            
            summary = ""
            for i, r in enumerate(results, 1):
                summary += f"{i}. {r['title']}\n{r['body']}\n\n"
            
            return summary.strip()
    except Exception as e:
        return f"Search failed: {str(e)}"