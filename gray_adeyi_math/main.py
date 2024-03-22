from enum import Enum


class Algorithm(str, Enum):
    RECURSIVE = "recursive"
    LOOP = "loop"


ALGORITHM = Algorithm.RECURSIVE


def power_recursive(base: int, exponent: int) -> int:
    if base <= 0:
        raise ValueError("invalid value for base")
    if exponent < 0:
        raise ValueError("cannot calcualte negative exponents")
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)


def power_loop(base: int, exponent: int) -> int:
    if base <= 0:
        raise ValueError("invalid value for base")
    result = 1
    while exponent >= 1:
        result *= base
        exponent -= 1
    return result


def power(base: int, exponent: int) -> int:
    return {Algorithm.RECURSIVE: power_recursive, Algorithm.LOOP: power_loop}[
        ALGORITHM
    ](base, exponent)


def factorial_recursive(value: int) -> int:
    if value <= 0:
        raise ValueError("invalid value passed in")
    if value == 1:
        return 1
    else:
        return value * factorial_recursive(value - 1)


def factorial_loop(value: int) -> int:
    if value <= 0:
        raise ValueError("invalid value passed in")
    result = 1
    while value > 1:
        result *= value
        value -= 1
    return value


def factorial(value: int) -> int:
    return {Algorithm.RECURSIVE: factorial_recursive, Algorithm.LOOP: factorial_loop}[
        ALGORITHM
    ](value)


def permutation(n: int, r: int) -> int:
    """Calculates the permutation from the provided values"""
    return factorial(n) / factorial(n - r)


def combination(n: int, r: int) -> int:
    """Calculates the combination from the provided values"""
    return permutation(n, r) * (1 / factorial(r))
