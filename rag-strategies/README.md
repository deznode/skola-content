# RAG Strategies Examples

Code examples demonstrating Retrieval-Augmented Generation (RAG) implementation patterns.

## Prerequisites

- Python 3.10+
- OpenAI API key or compatible LLM provider
- Vector database (Pinecone, Weaviate, or Chroma)

## Setup

```bash
cd examples/

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY=your-key-here
```

## Examples

| File | Description |
|------|-------------|
| `basic_rag.py` | Simple RAG pipeline |
| `chunking.py` | Document chunking strategies |
| `embedding.py` | Embedding generation |
| `retrieval.py` | Vector similarity search |
| `reranking.py` | Result reranking techniques |
| `hybrid_search.py` | Combining keyword and vector search |

## Structure

```
rag-strategies/
├── README.md
└── examples/
    ├── basic_rag.py
    ├── chunking.py
    └── ...
```

## Reference

See the full reference at: [skola.dev/references/rag-strategies](https://skola.dev/references/rag-strategies)
