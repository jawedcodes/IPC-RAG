
def build_prompt(query, context):
    return f"""
You are an IPC legal assistant. Use ONLY the following retrieved sections to answer.

Context:
{context}

Question:
{query}

Answer in concise, exact legal reasoning.
"""


