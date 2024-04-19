from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os
import shutil

FAISS_PATH = "faiss"
DATA_PATH = "docs"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_faiss(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_faiss(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(FAISS_PATH):
        shutil.rmtree(FAISS_PATH)

    # Initilize embedding model
    embeddings = OllamaEmbeddings(model="mxbai-embed-large") 

    # Create a new DB from the documents.
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(FAISS_PATH)
    print(f"Saved {len(chunks)} chunks to {FAISS_PATH}.")


if __name__ == "__main__":
    main()
