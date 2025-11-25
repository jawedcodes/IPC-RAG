from huggingface_hub import InferenceClient
from rag_system.config import HF_TOKEN, MODEL_ID

hf = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

def call_llm(prompt):
    res = hf.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.0
    )
    return res.choices[0].message["content"]
