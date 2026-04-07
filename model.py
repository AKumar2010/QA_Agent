
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

doc=['jjj','ioi']
def get_llm():
    load_dotenv()
    llm=ChatOpenAI(model='gpt-5.4-mini',temperature=0.4)
    return llm


    