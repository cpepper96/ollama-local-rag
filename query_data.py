import argparse
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

FAISS_PATH = "faiss"

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Initialize LLM
    llm = Ollama(model="llama2:13b")

    # Initialize embedding model
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    # Create vector object from local vector store
    vector = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    # Set up chain
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    # Set up retiever
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Invoke using RAG
    response = retrieval_chain.invoke({"input": query_text})
    print(response["answer"])


if __name__ == "__main__":
    main()