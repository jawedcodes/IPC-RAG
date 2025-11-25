from rag_system.retriever import search
from rag_system.prompt import build_prompt
from rag_system.llm import call_llm
from rag_system.context import build_context



def rag_answer(query, top_k=5):
    results = search(query, top_k)
    context = build_context(results)
    prompt = build_prompt(query, context)

    return call_llm(prompt=prompt)

