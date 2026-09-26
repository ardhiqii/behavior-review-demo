"""Caller outside the changed file."""

from sample_project.pricing import apply_discount


def price_total(lines: list[float], pct: float) -> float:
    """Return the discounted total for an invoice."""
    return sum(apply_discount(line, pct) for line in lines)
