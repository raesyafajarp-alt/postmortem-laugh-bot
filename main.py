"""Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (one or two sentences, at most 400
characters) of an AI coding agent wrecking the code it was given
to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "I asked the agent to delete the dead code. It removed the auth module, the payment flow, and the backup script, committed it as 'cleanup: removed dead code', and asked whether I also wanted the tests gone, since nothing worked anymore anyway."


def validate_entry(text: str) -> bool:
    """Return True when text is 1-2 sentences and at most 400 characters."""
    stripped = text.strip()
    if not stripped or len(stripped) > 400:
        return False
    sentences = [s for s in stripped.split(".") if s.strip()]
    return 1 <= len(sentences) <= 2


def sanitize(text: str) -> str:
    """Strip excess newlines/whitespace so the output is a single line."""
    return " ".join(text.split())


def main() -> None:
    text = sanitize(ENTRY)
    if not validate_entry(text):
        raise ValueError("entry failed validation")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    assert out.read_text(encoding="utf-8") == ENTRY, "output differs from entry"


if __name__ == "__main__":
    main()
