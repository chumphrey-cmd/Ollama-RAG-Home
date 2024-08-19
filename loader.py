import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def load_and_split_documents(directory_path="data"):
    """
    Loads all PDF documents from a directory and splits them into chunks.
    
    """
    ###___This option can be modified to ready any other documents desired.___###

    loader = DirectoryLoader(directory_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    all_docs = text_splitter.split_documents(documents)
    return all_docs
