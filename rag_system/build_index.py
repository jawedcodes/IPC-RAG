import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("thenlper/gte-small")

vectors = []
metadatas = []

with open("ipc_clean_sections.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)

        section = item["section_number"]
        text = item["text"]

        # Your embedding input
        content = f"Section {section}: {text}"

        emb = model.encode(content, convert_to_numpy=True)
        vectors.append(emb)
        metadatas.append(item)  # full metadata

# convert to 2D np array
vectors = np.vstack(vectors).astype("float32")

index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

faiss.write_index(index, "ipc_faiss.index")

with open("ipc_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadatas, f, ensure_ascii=False, indent=2)