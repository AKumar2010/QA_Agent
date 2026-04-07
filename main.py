
from utils.utility import load_apiKey
from agent.agent import load_dotenv, llm
from agent.rag import create_embedding
from langchain.agents import create_agent
from model import doc

def execute():
    #model=llm
    #load_apiKey()
    #get_llm_output()``
    print("execution in progress")
    #agent= create_agent(model=llm,system_prompt='you are helpful assistant')
    #agent.invoke()
    print(doc)
    


execute()