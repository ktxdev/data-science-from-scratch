import math
from typing import List
from collections import Counter

from linalg import dot, sum_of_squares


# Central Tendency functions
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


def quantile(xs: List[float], p: float) -> float:
    """Return the pth-percentile value in xs."""
    p_index = int(len(xs) * p)
    return xs[p_index]


def mode(xs: List[float]) -> List[float]:
    """Return the mode of a list of numbers."""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


# Dispersion functions
def data_range(xs: List[float]) -> float:
    """Return the range of a list of numbers."""
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """Return the standard deviation of a list of numbers."""
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    """Compute the interquartile range of a list of numbers."""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


# Correlation
def covariance(xs: List[float], ys: List[float]) -> float:
    """Calculate the covariance of 2 lists of numbers."""
    assert len(xs) == len(ys), "Lengths of xs and ys must match"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlation(xs: List[float], ys: List[float]) -> float:
    """Calculate the correlation of 2 lists of numbers."""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0