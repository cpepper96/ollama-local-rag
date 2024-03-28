# Langchain RAG Tutorial

This repository provides an example of implementing Retrieval-Augmented Generation (RAG) using LangChain and Ollama. The RAG approach combines the strengths of an LLM with a retrieval system (in this case, FAISS) to allow the model to access and incorporate external information during the generation process.

## LangChain

[LangChain](https://github.com/langchain-ai/langchain) is a framework for developing applications with LLMs. It provides a modular and extensible approach to building applications, allowing you to combine different components (e.g., LLMs, retrieval systems, data sources) in a flexible manner.

## FAISS

[FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search) is a library for efficient similarity search and dense vector clustering. In this example, we use FAISS as the retrieval system to store and search through text data.

## Ollama

[Ollama](https://github.com/ollama/ollama) is a tool for running large language models locally. Supported models are listed [here](https://ollama.com/library).

## Getting Started

To get started with this example, follow these steps:

Install python dependencies:

```python
pip3 install -r requirements.txt
```

Start Ollama with a model of you choice:

```bash
ollama run llama2:13b
```

>NOTE: This model needs to match the model referenced in the python code.

Create the FAISS database:

```python
python3 create_database.py
```

This script reads files from a directory (specified in the script) and creates a FAISS index.

Query the FAISS database.

```python
python3 query_data.py "What is Amazon Bedrock?"
```

This script takes a query as input, uses the LangChain [retrieval](https://python.langchain.com/docs/modules/data_connection/) to retrieve relevant information from the FAISS database, and generates a response using an LLM (specified in the script).
