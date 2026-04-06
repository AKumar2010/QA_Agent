
from langchain_community.document_loaders  import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from utils.utility import load_apiKey
from langchain_openai import ChatOpenAI
import os

#retrieval_qa, retrieval, RetrievalQAWithSourcesChain
docs=[]
def readpdf_files():

    resources= os.path.abspath("resources")
    for f in os.listdir(resources):
        file=os.path.join(resources,f)
        docs.append(file)
    print (docs)




#need to check why append method not work.
def chunkAll()-> list[Document]:
        documents_after_load=[]
        
        resources= os.path.abspath("resources")
        document_loader = PyPDFDirectoryLoader(resources)
        documents_after_load= document_loader.load()
        print("length of docs loaded.",len(documents_after_load))

        split=RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
        splitted_docs=split.split_documents(documents_after_load)
        #final_doc=split.create_documents(splitted_docs)
       # print(splitted_docs)
        return splitted_docs



def create_embedding():
     load_apiKey()
     _llm= ChatOpenAI(model='gpt-5.4-mini',temperature=0.4)
     context="spacex starship. NeTflix Architecture"
     rule="Asssume you are an assistant which search info from docs.You have to check the {context} and answer {input}"
     
     template=ChatPromptTemplate.from_template("""
                                               Asssume you are an assistant which search info from docs. 
                                               You have to provide answer from asked {input} with given {context} 
                                               """)
     print("input variables are:",template.input_variables)
     userinput= input("enter your topic to search from documets..")
     embedding=OpenAIEmbeddings(model='text-embedding-3-small')
     ch_db=Chroma(embedding_function=embedding,persist_directory='./qa_db').from_documents(chunkAll(),embedding,persist_directory='./qa_db')
     retriever = ch_db.as_retriever()
     ch_db.similarity_search("Check the starship spacex documents and let me know the details about Raptor 2 engines")
     doc_chain=create_stuff_documents_chain(_llm,template)
     retieval_chain= create_retrieval_chain(retriever,doc_chain)
     response=retieval_chain.invoke({"input":userinput,"context":context})
     print(response.get('answer'))
     





create_embedding()
    