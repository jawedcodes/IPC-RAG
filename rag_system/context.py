def build_context(results):
    context_parts = []
    for item in results:
        section = item["section_number"]
        text = item["text"]
        context_parts.append(f"Section {section}: {text}")
    return "\n\n".join(context_parts)

