from typing import Callable

from PIL.ImagePalette import random

from linalg import Vector, distance, add, scalar_multiply, vector_mean


# def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
#     return (f(x + h) - f(x)) / h
#
#
# def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float) -> float:
#     """Returns the i-th partial difference quotient of f at v"""
#     w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
#     return (f(w) - f(v)) / h
#
#
# def estimate_gradient(f: Callable[[Vector], float], v: Vector, h: float = 0.00001):
#     return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size` in the `gradient` direction from v"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = (predicted - y)
    squared_error = error ** 2
    return [2 * error * x, 2 * error]

if __name__ == "__main__":
    import random

    v = [random.uniform(-10, 10) for _ in range(3)]

    for epoch in range(1000):
        grad = sum_of_squares_gradient(v)
        v = gradient_step(v=v, gradient=grad, step_size=-0.01)
        print(epoch, v)

    assert distance(v, [0, 0, 0]) < 0.001

    inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
    theta = [random.uniform(-1, 1), random.uniform(-1,1)]

    learning_rate = 0.001

    for epoch in range(5000):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)

    slope, intercept = theta
    assert 19.9 < slope < 20.1, "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"
