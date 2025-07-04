from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

llm = OllamaLLM(model="phi3")

query = input("What can I help you research? ").strip()

if not query:
    print("Please enter a valid question.")
    exit()

# Try Wikipedia first
print("🔎 Fetching information from Wikipedia...")
search_result = wiki_tool.run(query)

# Fallback to DuckDuckGo if Wikipedia result is too short
if not search_result or len(search_result.strip()) < 50:
    print("⚠️ Wikipedia didn't return much. Trying DuckDuckGo...")
    search_result = search_tool.run(query)

# Create prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant. Read the following search data and generate a short, clear research summary for beginners."
        ),
        ("human", "{data}")
    ]
)
formatted_prompt = prompt.format_messages(data=search_result)

# Get LLM response
response = llm.invoke(formatted_prompt)

# Output & Save
print("\n📝 Summary:\n", response)
save_tool.run(response)
