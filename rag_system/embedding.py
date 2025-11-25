
from sentence_transformers import SentenceTransformer
import faiss
import json
from rag_system.config import EMBED_MODEL, METADATA_PATH

embedder = SentenceTransformer(EMBED_MODEL)

def load_metadata():
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    if isinstance(meta, dict):
        meta = list(meta.values())
    return meta

def embed_query(q: str):
    emb = embedder.encode([q], convert_to_numpy=True)
    emb = emb.astype("float32")
    faiss.normalize_L2(emb)
    return emb
