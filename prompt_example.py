"""Example: build a prompt from a template.

Usage:
    python3 prompt_example.py
"""

TEMPLATES = {
    "explain": (
        "Explain {topic} to someone who has never seen it before. "
        "Start with the core idea in plain language, define any "
        "technical term as it appears, and use one concrete example."
    ),
    "summarize": (
        "Summarize the text below. Lead with the bottom line, then "
        "the supporting points, then anything unresolved. "
        "Do not add facts that are not in the text.\n\n{text}"
    ),
}


def build(kind, **kwargs):
    return TEMPLATES[kind].format(**kwargs)


if __name__ == "__main__":
    print(build("explain", topic="ETL in data engineering"))
    print()
    print(build("summarize", text="Paste your text here."))