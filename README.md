# Salary Insights Agent using MCP

An AI-powered Salary Insights Agent built using **LangChain, Google Gemini, MCP (Model Context Protocol), and Firecrawl**.

The agent searches salary websites and extracts compensation information for specific skills, including internship stipends, fresher salaries, experience-wise salaries, city-wise comparisons, and company-wise compensation.

## Features

- Search the web for salary information
- Scrape salary websites using Firecrawl
- Find internship stipends and fresher salaries
- Analyze salary by experience level
- Compare salaries across cities
- Identify company-wise compensation
- Extract additional compensation such as bonuses and stock options
- Identify skills that can improve salary
- Uses MCP to connect LangChain with Firecrawl tools

## Tech Stack

- Python
- LangChain
- Google Gemini
- MCP (Model Context Protocol)
- Firecrawl
- python-dotenv
- LangGraph

## Project Architecture

User Query
    ↓
LangChain Agent
    ↓
Google Gemini
    ↓
MCP Client
    ↓
Firecrawl MCP Server
    ↓
Search / Scrape Salary Websites
    ↓
Salary Insights
    ↓
User

## MCP Tools Used

The project connects to Firecrawl through MCP.

The main tools used by the agent are:

- firecrawl_search
- firecrawl_scrape

Only the required Firecrawl tools are passed to the agent to keep the tool set focused.

## Project Structure

```text
SalaryInsightsAgentusingMCP/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd SalaryInsightsAgentusingMCP
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install langchain langchain-google-genai langchain-mcp-adapters python-dotenv
```

### 4. Configure API Keys

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

Never commit the `.env` file to GitHub.

## Running the Project

Run:

```bash
python app.py
```

Example query:

```text
Search for Python developer internship stipend and salary in India.
Find data from salary websites showing monthly stipend for interns and freshers.
```

## Example Output

```text
SALARY BREAKDOWN BY EXPERIENCE

Entry Level (0-2 years):
Salary range based on scraped sources.

Mid Level (3-5 years):
Salary range based on scraped sources.

Senior Level (5+ years):
Salary range based on scraped sources.

CITY-WISE COMPARISON

Bangalore:
Salary range

Hyderabad:
Salary range

Mumbai:
Salary range

TOP PAYING COMPANIES

Company-wise salary information extracted from the sources.

ADDITIONAL COMPENSATION

Bonuses, stock options, and other benefits found in the scraped data.

SKILLS THAT BOOST SALARY

Additional skills and certifications that may improve compensation.
```

## Why MCP?

MCP allows the AI agent to connect with external tools in a standardized way.

In this project:

```text
LangChain Agent
      ↓
MCP Client
      ↓
Firecrawl MCP Server
      ↓
Firecrawl Tools
```

Instead of manually implementing every Firecrawl API operation, the agent can access the tools exposed by the MCP server.

## Environment Variables

The following environment variables are required:

```text
GOOGLE_API_KEY
FIRECRAWL_API_KEY
```

Do not expose API keys in source code or commit them to GitHub.

## Future Improvements

- Add more salary sources
- Add salary trend analysis
- Add skill-demand analysis
- Add job-market comparison
- Add location-based salary recommendations
- Build a web interface using React
- Store historical salary data
- Add charts for salary comparisons

## Author

Siva

## License

This project is for educational and learning purposes.
```
