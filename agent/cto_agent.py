import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_cto_prompt(startup_idea: str) -> str:
    return f"""
You are the CTO of a new startup. The startup idea is:

\"\"\"{startup_idea}\"\"\"

As the CTO, your responsibilities are:
1. Recommend a modern and scalable tech stack for the MVP.
2. Define the MVP's core features.
3. Break the MVP into a development plan (phases or sprints).
4. Identify major technical risks and propose mitigations.

Respond in the following format:
- Tech Stack:
- MVP Features:
- Development Plan:
- Technical Risks & Mitigations:
"""

def get_cto_response(startup_idea: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
    prompt = get_cto_prompt(startup_idea)
    return llm.invoke(prompt)

def run_cto_agent(startup_idea: str) -> str:
    print("\n[CTO AGENT] Analyzing the startup idea...\n")
    response = get_cto_response(startup_idea)
    print(response.content)
    return response

if __name__ == "__main__":
    
    example_idea = """- **Idea Name:**  PersonaPro

- **Problem:**  Businesses struggle to efficiently manage and leverage AI tools across departments, leading to fragmented workflows, data silos, and underutilized AI potential.  Employees lack personalized AI assistance tailored to their specific roles and skill levels.

- **Solution:** PersonaPro is a centralized AI platform that acts as a personalized "AI assistant manager" for businesses. It integrates with existing enterprise systems (like those targeted by Writer's AI HQ), automatically assigns AI agents (similar to Writer's agents) to specific tasks based on employee roles and project needs, and provides a user-friendly interface for managing and monitoring all AI activities.  It learns user preferences and adapts its recommendations over time, ensuring optimal AI utilization.  Think of it as a "concierge" for AI within a company.

- **Target Market:** Medium to large enterprises across various sectors (e.g., finance, marketing, customer service) looking to streamline operations, improve efficiency, and maximize ROI on AI investments.

- **Revenue Model:**  Subscription-based SaaS model, tiered based on the number of users, integrated systems, and AI agent capacity.  Premium tiers could offer advanced analytics and custom AI agent development.

- **Why Now (based on trends):**  The market is ripe for a solution like PersonaPro.  Writer's AI HQ demonstrates the growing demand for AI-powered workflow automation.  Phia's success highlights the consumer appetite for AI-driven shopping experiences, indicating a broader acceptance of AI in daily life.  Genies' avatar technology showcases the increasing personalization trend, which PersonaPro leverages by tailoring AI assistance to individual employees.  The Dutch tech scene's innovation (as highlighted in the TNW article) further supports the feasibility and potential for a sophisticated AI management platform.  PersonaPro's USP is its personalized, centralized management of diverse AI tools, addressing the current fragmentation and complexity of the enterprise AI landscape."
"""
    run_cto_agent(example_idea)