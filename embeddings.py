import chromadb
from sentence_transformers import SentenceTransformer

# Load model once (reused across calls)
_model = None
_client = None
_collection = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_collection():
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path="chroma_db")
        _collection = _client.get_or_create_collection(name="documents")
    return _collection


# Simple keyword-based auto-categorization (fast, no AI needed)
CATEGORY_KEYWORDS = {
    "AI/ML": ["ai", "machine learning", "ml", "deep learning", "nlp", "llm", "generative ai", "genai"],
    "Cloud": ["azure", "aws", "gcp", "cloud", "devops", "mlops"],
    "Web Development": ["react", "javascript", "html", "css", "frontend", "backend", "full stack"],
    "Data Science": ["data science", "data analysis", "pandas", "sql", "statistics"],
    "Internship": ["internship", "intern"],
    "Project": ["project", "built", "developed"],
}


def auto_tag(text: str) -> list:
    text_lower = text.lower()
    tags = []
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            tags.append(category)
    return tags if tags else ["General"]


def add_document_embedding(doc_id: int, title: str, description: str, doc_type: str):
    """Generate embedding for a document and store it in ChromaDB."""
    model = get_model()
    collection = get_collection()

    combined_text = f"{title}. {description}"
    embedding = model.encode(combined_text).tolist()

    collection.upsert(
        ids=[str(doc_id)],
        embeddings=[embedding],
        documents=[combined_text],
        metadatas=[{"title": title, "doc_type": doc_type}],
    )


def semantic_search(query: str, n_results: int = 5):
    """Search documents by meaning, not just keywords."""
    model = get_model()
    collection = get_collection()

    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )
    return results