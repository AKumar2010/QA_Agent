from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import AIMessagePromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
#from utils.utility import load_apiKey
import os

def get_llm_output():
    load_dotenv()
    #os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

    # messages=[("system","Assume You are having knowledge on all the things."),
    #           ("human","Write me a paragraph on Iran War.."),]
    messages=[SystemMessage(content="Assume You are having knowledge on all the things."),
              HumanMessage(content="Write me a paragraph on 1857 war..")]
    llm=ChatOpenAI(model='gpt-5.4-mini',temperature=0.4)
    #print(llm.invoke(messages))
    #llm.stream(messages)
    # output=llm.invoke(messages).content
    # print(output)


    prompt= PromptTemplate.from_template("give information about {topic}")
    usrinput= input("enter your topic..")
    myprompt=prompt.invoke({"topic":usrinput})
    print("prompt is: ",myprompt)
    info=llm.invoke(myprompt)
    print(info)

    print("end of line")


if __name__=="__main__":
    get_llm_output()
    