from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
@tool
def triple(num: float) -> float:
    """Triples a number."""
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash", temperature=0).bind_tools(tools)