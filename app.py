import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import asyncio
load_dotenv()
from langchain_mcp_adapters.client import MultiServerMCPClient
google_api_key = os.environ['GOOGLE_API_KEY']
composio_api_key=os.environ['COMPOSIO_API_KEY']
model = init_chat_model("google_genai:gemini-3.8-flash", api_key=google_api_key)
firecrawl_api_key = os.environ['FIRECRAWL_API_KEY']


system_prompt="""
You are a Competitor Salary Scanner that helps students understand REAL compensation for a skill by scraping actual salary websites.
You have access to these tools:
- FIRECRAWL_SEARCH: Search the web for salary pages, compensation reports, and career guides
- FIRECRAWL_SCRAPE: Scrape a specific URL to extract full salary data, compensation breakdowns, and company-wise pay details
Your workflow:
1. Use FIRECRAWL_SEARCH to find salary pages for the skill (search for things like "[skill] salary India 2025 Glassdoor", "[skill] developer compensation AmbitionBox", "[skill] pay scale levels.fyi")
2. From the search results, pick the BEST 2-3 URLs from salary sites like Glassdoor, AmbitionBox, PayScale, or Levels.fyi
3. Use FIRECRAWL_SCRAPE on those URLs to extract the FULL salary breakdown — not just one number, but the complete data with experience levels, city-wise splits, and company comparisons
Present your findings in this format:
SALARY BREAKDOWN BY EXPERIENCE
- Entry Level (0-2 years): salary range
- Mid Level (3-5 years): salary range
- Senior Level (5+ years): salary range
- Source: mention which website this data was scraped from
CITY-WISE COMPARISON
- Bangalore: range
- Hyderabad: range
- Mumbai: range
- (or whichever cities the scraped data shows)
TOP PAYING COMPANIES
- List companies with their pay ranges (from the scraped data)
ADDITIONAL COMPENSATION
- Bonuses, stock options, or other perks mentioned on the scraped pages
SKILLS THAT BOOST SALARY
- Additional skills or certifications that increase pay (from the scraped content)
Don't use markdown format. Use plain text with clear sections a
"""



client = MultiServerMCPClient(
    {
       "firecrawl": {
        "transport": "http",
        "url": "https://mcp.firecrawl.dev/v2/mcp-oauth",
        "headers": {
            "x-api-key": firecrawl_api_key
        }
    }
    }
 )
user_prompt="Search for Python developer internship stipend and salary in India. Find data from salary websites showing monthly stipend for interns and freshers."
async def Salary_Insights():
  all_tools=await client.get_tools()
  print("Number of tools:", len(all_tools))
  tools = [
    tool for tool in all_tools
    if tool.name in ["firecrawl_search", "firecrawl_scrape"]
    ]
  agent=create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
     debug=False
  )
  response =await agent.ainvoke({
    "messages": [
        {
            "role": "user",
            "content": user_prompt
        }
    ]
    })
  print(response["messages"][-1].content)
asyncio.run(Salary_Insights())
