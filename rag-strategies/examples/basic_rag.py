"""
Basic RAG Pipeline Example
Demonstrates a simple retrieval-augmented generation workflow.
"""
from typing import List
import os

# Note: Install with: pip install openai chromadb

from openai import OpenAI
import chromadb


def create_embeddings(client: OpenAI, texts: List[str]) -> List[List[float]]:
    """Generate embeddings for a list of texts."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]


def create_vector_store(documents: List[str]) -> chromadb.Collection:
    """Create an in-memory vector store with documents."""
    client = chromadb.Client()
    collection = client.create_collection(name="docs")

    # Add documents with auto-generated IDs
    collection.add(
        documents=documents,
        ids=[f"doc_{i}" for i in range(len(documents))]
    )

    return collection


def retrieve_relevant_docs(
    collection: chromadb.Collection,
    query: str,
    n_results: int = 3
) -> List[str]:
    """Retrieve the most relevant documents for a query."""
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0]


def generate_response(
    client: OpenAI,
    query: str,
    context: List[str]
) -> str:
    """Generate a response using retrieved context."""
    context_text = "\n\n".join(context)

    messages = [
        {
            "role": "system",
            "content": """You are a helpful assistant. Answer the user's question
            based on the provided context. If the context doesn't contain
            relevant information, say so."""
        },
        {
            "role": "user",
            "content": f"""Context:
{context_text}

Question: {query}

Answer based on the context above:"""
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


def rag_pipeline(query: str, documents: List[str]) -> str:
    """Complete RAG pipeline: retrieve + generate."""
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Create vector store
    collection = create_vector_store(documents)

    # Retrieve relevant documents
    relevant_docs = retrieve_relevant_docs(collection, query)

    # Generate response
    response = generate_response(client, query, relevant_docs)

    return response


# Example usage
if __name__ == "__main__":
    # Sample documents
    documents = [
        "Python was created by Guido van Rossum and first released in 1991.",
        "Python is known for its simple, readable syntax that emphasizes code clarity.",
        "Popular Python frameworks include Django for web development and PyTorch for ML.",
        "Python uses dynamic typing and garbage collection for memory management.",
        "The Python Package Index (PyPI) hosts over 400,000 packages."
    ]

    # Query
    query = "Who created Python and when?"

    # Run pipeline
    response = rag_pipeline(query, documents)
    print(f"Query: {query}")
    print(f"Response: {response}")
