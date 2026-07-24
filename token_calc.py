"""Token cost calculator — QA E2E test module (AI-authored)."""


def raw_tokens(usage: dict) -> int:
    """Sum billable token components the backend attributes."""
    return (
        usage.get("input_tokens", 0)
        + usage.get("output_tokens", 0)
        + usage.get("cache_read_input_tokens", 0)
        + usage.get("cache_creation", {}).get("ephemeral_5m_input_tokens", 0)
        + usage.get("cache_creation", {}).get("ephemeral_1h_input_tokens", 0)
    )


def cost_usd(tokens: int, rate_per_mtok: float) -> float:
    return round(tokens / 1_000_000 * rate_per_mtok, 4)
