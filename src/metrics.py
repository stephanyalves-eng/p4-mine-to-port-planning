"""Shared industrial engineering metrics."""


def oee(availability: float, performance: float, quality: float) -> float:
    """Overall Equipment Effectiveness: availability x performance x quality, each in [0, 1]."""
    for name, value in (
        ("availability", availability),
        ("performance", performance),
        ("quality", quality),
    ):
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1, got {value}")
    return availability * performance * quality
