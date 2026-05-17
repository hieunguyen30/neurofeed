from sentence_transformers import SentenceTransformer

_model: SentenceTransformer | None = None


def load_model() -> None:
    global _model
    _model = SentenceTransformer("all-MiniLM-L6-v2")


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        load_model()
    return _model


def embed_text(text: str) -> list[float]:
    """Return a normalized 384-dim embedding for the given text."""
    return _get_model().encode(text, normalize_embeddings=True).tolist()
