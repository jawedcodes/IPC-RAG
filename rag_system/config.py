import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = os.getenv("MODEL_ID", "meta-llama/Llama-3.1-8B-Instruct")
EMBED_MODEL = os.getenv("EMBED_MODEL", "thenlper/gte-small")
FAISS_INDEX_PATH = os.getenv("FAISS_HNSW_PATH", "ipc_faiss.index")
METADATA_PATH = os.getenv("METADATA_PATH", "ipc_metadata.json")
TOP_K = int(os.getenv("TOP_K", "6"))