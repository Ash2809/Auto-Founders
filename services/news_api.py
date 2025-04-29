import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  
NEWS_API_URL = "https://newsapi.org/v2/everything"

def get_market_trends():
    query = "AI startups OR technology market OR funding trends"
    
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 6 
    }

    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        
        trends = []
        for article in articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description available")
            
            trends.append(f"**{title}**\n{description}")
        
        return "\n\n".join(trends)
    else:
        print(f"Error fetching market trends: {response.status_code}")
        return "Failed to fetch market trends."


if __name__ == "__main__":
    trends = get_market_trends()
    print(trends)