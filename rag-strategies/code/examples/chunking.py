"""
Document Chunking Strategies
Different approaches to splitting documents for RAG systems.
"""
from typing import List, Callable
from dataclasses import dataclass


@dataclass
class Chunk:
    """Represents a document chunk with metadata."""
    content: str
    index: int
    metadata: dict = None


def fixed_size_chunking(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[Chunk]:
    """
    Split text into fixed-size chunks with overlap.

    Args:
        text: The text to chunk
        chunk_size: Maximum characters per chunk
        overlap: Characters to overlap between chunks

    Returns:
        List of Chunk objects
    """
    chunks = []
    start = 0
    index = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append(Chunk(
            content=chunk_text.strip(),
            index=index,
            metadata={"start": start, "end": end}
        ))

        start = end - overlap
        index += 1

    return chunks


def sentence_chunking(
    text: str,
    max_sentences: int = 5,
    overlap_sentences: int = 1
) -> List[Chunk]:
    """
    Split text by sentences with overlap.

    Args:
        text: The text to chunk
        max_sentences: Maximum sentences per chunk
        overlap_sentences: Sentences to overlap between chunks
    """
    # Simple sentence splitting (for production, use spaCy or NLTK)
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    index = 0
    i = 0

    while i < len(sentences):
        chunk_sentences = sentences[i:i + max_sentences]
        chunk_text = ' '.join(chunk_sentences)

        chunks.append(Chunk(
            content=chunk_text,
            index=index,
            metadata={
                "sentence_start": i,
                "sentence_end": i + len(chunk_sentences)
            }
        ))

        i += max_sentences - overlap_sentences
        index += 1

    return chunks


def semantic_chunking(
    text: str,
    headers: List[str] = None
) -> List[Chunk]:
    """
    Split text by semantic boundaries (headers, paragraphs).

    Args:
        text: The text to chunk
        headers: Optional list of header markers to split on
    """
    if headers is None:
        headers = ["# ", "## ", "### ", "\n\n"]

    import re
    # Create pattern from headers
    pattern = '|'.join(re.escape(h) for h in headers)
    sections = re.split(f'({pattern})', text)

    chunks = []
    current_chunk = ""
    index = 0

    for section in sections:
        if section.strip():
            if any(section.startswith(h) for h in headers):
                # Save current chunk if exists
                if current_chunk.strip():
                    chunks.append(Chunk(
                        content=current_chunk.strip(),
                        index=index
                    ))
                    index += 1
                current_chunk = section
            else:
                current_chunk += section

    # Don't forget the last chunk
    if current_chunk.strip():
        chunks.append(Chunk(
            content=current_chunk.strip(),
            index=index
        ))

    return chunks


def recursive_chunking(
    text: str,
    max_chunk_size: int = 1000,
    separators: List[str] = None
) -> List[Chunk]:
    """
    Recursively split text using a hierarchy of separators.
    Tries larger separators first, then smaller ones.

    Args:
        text: The text to chunk
        max_chunk_size: Maximum chunk size
        separators: Ordered list of separators (largest to smallest)
    """
    if separators is None:
        separators = ["\n\n", "\n", ". ", " "]

    def split_recursive(text: str, sep_index: int) -> List[str]:
        if len(text) <= max_chunk_size:
            return [text]

        if sep_index >= len(separators):
            # No more separators, force split
            return [text[i:i + max_chunk_size]
                    for i in range(0, len(text), max_chunk_size)]

        separator = separators[sep_index]
        parts = text.split(separator)

        result = []
        current = ""

        for part in parts:
            potential = current + separator + part if current else part

            if len(potential) <= max_chunk_size:
                current = potential
            else:
                if current:
                    result.extend(split_recursive(current, sep_index + 1))
                current = part

        if current:
            result.extend(split_recursive(current, sep_index + 1))

        return result

    text_chunks = split_recursive(text, 0)
    return [
        Chunk(content=chunk.strip(), index=i)
        for i, chunk in enumerate(text_chunks)
        if chunk.strip()
    ]


# Example usage
if __name__ == "__main__":
    sample_text = """
    # Introduction to RAG

    Retrieval-Augmented Generation (RAG) is a technique that combines
    retrieval-based and generation-based approaches. It first retrieves
    relevant documents from a knowledge base, then uses them to generate
    accurate responses.

    ## Why Use RAG?

    RAG helps overcome the knowledge cutoff limitation of LLMs. It provides
    factual grounding and reduces hallucinations. The retrieved context
    gives the model specific information to work with.

    ## Implementation Steps

    First, prepare your document corpus. Then create embeddings for all
    documents. Store them in a vector database. When a query comes in,
    retrieve relevant documents. Finally, pass them to the LLM for generation.
    """

    print("=== Fixed Size Chunking ===")
    chunks = fixed_size_chunking(sample_text, chunk_size=200, overlap=20)
    for chunk in chunks:
        print(f"[{chunk.index}] {chunk.content[:50]}...")

    print("\n=== Semantic Chunking ===")
    chunks = semantic_chunking(sample_text)
    for chunk in chunks:
        print(f"[{chunk.index}] {chunk.content[:50]}...")
