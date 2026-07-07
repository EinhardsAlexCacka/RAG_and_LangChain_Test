import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (TextLoader, PyPDFLoader, WebBaseLoader)
from bs4 import SoupStrainer

from dotenv import load_dotenv

load_dotenv()

def load_text_file():
    # Create a temporary text file for demonstration
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"Hello, this is a sample text file.\nThis file is used to test the system that is built")
        temp_file_path = temp_file.name
        
    try:
        # Load the text file using TextLoader
        loader = TextLoader(temp_file_path)
        documents = loader.load()
        
        print(f"Loaded {len(documents)} document(s)")
        print(f"Content preview: {documents[0].page_content[:100]}...")
        print(f"Metadata: {documents[0].metadata}")
        
        # Print the loaded documents
        #for doc in documents:
        #    print("Document Content:")
        #    print(doc)
        #    print(doc.page_content)
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

def pdf_loader(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    print(f"Loaded {len(documents)} document(s) from PDF")
    for i, doc in enumerate(documents):
        print(f"Document {i+1} Content Preview: {doc.page_content[:100]}...")
        print(f"Metadata: {doc.metadata}")

def web_loader():
    loader = WebBaseLoader(
        "https://en.wikipedia.org/wiki/Web_scraping", bs_kwargs={
            "parse_only": SoupStrainer(id="mw-content-text")
        }
    )
    documents = loader.load()
    
    print(f"Loaded {len(documents)} document(s) from web")
    print(f"Source: {documents[0].metadata.get('source', 'N/A')}")
    print(f"Content lenght: {len(documents[0].page_content)} characters")
    print(f"Preview: {documents[0].page_content[:200]}...")
     
if __name__ == "__main__":
    #load_text_file()
    #pdf_loader("./docs/langchain_demo.pdf")
    web_loader()