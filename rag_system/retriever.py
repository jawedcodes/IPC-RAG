from rag_system.config import EMBED_MODEL
from sentence_transformers import SentenceTransformer
from rag_system.build_index import index, metadatas


embedder = SentenceTransformer(EMBED_MODEL)

def search(q, top_k=7):
    emb = embedder.encode(q, convert_to_numpy=True).astype("float32")
    emb = emb.reshape(1, -1)

    scores, ids = index.search(emb, top_k)

    results = []
    for i, score in zip(ids[0], scores[0]):
        meta = metadatas[i]
        results.append({
            "section_number": meta["section_number"],
            "text": meta["text"],
            "score": float(score)
        })
    return results
