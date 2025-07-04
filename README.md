## ACKNOWLEDGEMENT
This project is inspired by (https://github.com/techwithtim/PythonAIAgentFromScratch.git).
Their work laid the foundation for this research bot and I have modified it for offline use and simplicity.

# Local Research Chatbot using Ollama

A simple research assistant chatbot powered by `phi3` running locally using **Ollama**.  
It fetches info from Wikipedia and DuckDuckGo, summarizes it with an LLM, and saves your research.

## Setup Instructions

1. Clone this repo

2. Create and Activate a Virtual Environment

3. Install Dependencies
   `pip install -r requirements.txt`
   This will install:
   langchain
   langchain-community
   langchain-ollama
   python-dotenv
   wikipedia
   pydantic
   duckduckgo-search (installed as a sub-dependency)

4. Install and Run Ollama
   `ollama run phi3`

5. Configure Environment Variables (Optional)
   If you later decide to use APIs like OpenAI or Anthropic, you can use a .env file.

   For now, since **Ollama** is local, you don’t need any API keys.

6. Run the Application
   `python main.py`
   You’ll be prompted with:
   "What can I help you research?"
   Type your query and get a clean summary. The response will also be saved to research_output.txt.

## How It Works
  Gets input from user

  Searches Wikipedia / DuckDuckGo

  Passes data to phi3 LLM

  Summarizes the result

  Saves the research output to a .txt file
