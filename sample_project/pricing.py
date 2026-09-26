"""Pricing rules for the Behavior Review fixture."""


def apply_discount(amount: float, pct: float) -> float:
    """Apply a percentage discount and keep currency precision."""
    return round(amount * (1 - pct / 100), 1)
