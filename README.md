# Langchain RAG Tutorial

This repository provides an example of using the Retrieval-Augmented Generation (RAG) approach from LangChain, a powerful Python library for building applications with large language models (LLMs). The RAG approach combines the strengths of an LLM with a retrieval system (in this case, FAISS) to allow the model to access and incorporate external information during the generation process.

## LangChain

[LangChain](https://github.com/hwchase17/langchain) is a framework for developing applications with LLMs. It provides a modular and extensible approach to building applications, allowing you to combine different components (e.g., LLMs, retrieval systems, data sources) in a flexible manner.

## FAISS

[FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search) is a library for efficient similarity search and dense vector clustering. In this example, we use FAISS as the retrieval system to store and search through text data.

## Ollama



## Getting Started

To get started with this example, follow these steps:

1. Install dependencies:

```python
pip3 install -r requirements.txt
```

Query the FAISS database:

```python
python3 create_database.py
```

This script reads files from a directory (specified in the script) and creates a FAISS index.

Query the FAISS DB.

```python
python3 query_data.py "What is Amazon Bedrock?"
```
This script takes a query as input, uses the LangChain RAG approach to retrieve relevant information from the FAISS database, and generates a response using an LLM (specified in the script).
