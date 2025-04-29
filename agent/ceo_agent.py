import sys
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from services.news_api import get_market_trends
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.2)

prompt = PromptTemplate(
    input_variables=["trends"],
    template="""
You are a seasoned startup mentor and tech visionary.

Based on the following recent market trends:
{trends}

Suggest a compelling startup idea that:
1. Solves a real-world problem.
2. Is technically feasible in 2025.
3. Has a clear target market and potential business model.
4. Includes a unique selling point (USP).
5. Explains how the product leverages the current trends.

Format your response with:
- Idea Name
- Problem
- Solution
- Target Market
- Revenue Model
- Why Now (based on trends)

Be concise, actionable, and insightful.
"""
)

def generate_startup_idea():
    market_trends = get_market_trends()
    formatted_prompt = prompt.format(trends=market_trends)
    idea = llm.invoke(formatted_prompt)
    print("\nStartup Idea Generated:\n")
    print(idea.content)

if __name__ == "__main__":
    generate_startup_idea()
