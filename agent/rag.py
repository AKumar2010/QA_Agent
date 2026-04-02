
from langchain_community.document_loaders  import  PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os

docs=[]
def readpdf_files():
    
    resources= os.path.abspath("resources")
    for f in os.listdir(resources):
        file=os.path.join(resources,f)
        docs.append(file)
    print (docs)

def loadAll():
    for doc in docs:
        loader=PyPDFLoader(doc)
        loader.load()
    return loader

#need to check why append method not work.
def chunkAll()-> list[Document]:
        documents_after_load=[]
        for doc in docs:
            loader=PyPDFLoader(doc)
            documents_after_load.extend(loader.lazy_load())
        print(documents_after_load)
        
        split=RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
        splitted_docs=split.split_documents(documents_after_load)
        #final_doc=split.create_documents(splitted_docs)
        print(splitted_docs)
        return splitted_docs

def create_embedding():
     
     embedding=OpenAIEmbeddings(model='text-embedding-3-small')
     ch_db=Chroma(embedding,persist_directory='./qa_db').from_documents(chunkAll())
     
     


    






readpdf_files()
create_embedding()
    