from typing import List

def mean(xs: List[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(xs) / len(xs)

def _median_odd(xs: List[float]) -> float:
    """Calculate the median of a list of numbers if the length of list is odd."""
    return sorted(xs)[int(len(xs) / 2)]

def _median_even(xs: List[float]) -> float:
    """Calculate the median of a list of numbers if the length of list is even."""
    sorted_xs = sorted(xs)
    hi_midpoint = len(sorted_xs) // 2
    return (sorted_xs[hi_midpoint] + sorted_xs[hi_midpoint - 1]) / 2

def median(xs: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)

if __name__ == "__main__":
    # Testing median
    assert median([1, 10, 2, 9, 5]) == 5
    assert median([1, 9, 2, 10]) == (2 + 9) / 2