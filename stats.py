from typing import List

def mean(xs: List[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(xs) / len(xs)