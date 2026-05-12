"""Teste random reproductibile pentru linear_search(v, key)."""

import random

import pytest

from linear_search import linear_search
from tests.oracle import oracle_linear_search


N = 1000
LOWER_BOUND = -10
UPPER_BOUND = 10
LIST_LENGTH = 5
SEED = 42


def generate_random_cases(n: int):
    """
    Genereaza n cazuri de test aleatoare, reproductibile.

    Fiecare caz contine:
        - o lista v cu exact 5 numere intregi;
        - o valoare key din acelasi interval.
    """
    generator = random.Random(SEED)
    cases = []

    for _ in range(n):
        v = [
            generator.randint(LOWER_BOUND, UPPER_BOUND)
            for _ in range(LIST_LENGTH)
        ]
        key = generator.randint(LOWER_BOUND, UPPER_BOUND)
        cases.append((v, key))

    return cases


TEST_CASES = generate_random_cases(N)


@pytest.mark.parametrize("v, key", TEST_CASES)
def test_random_linear_search(v, key):
    expected = oracle_linear_search(v, key)
    obtained = linear_search(v, key)

    assert obtained == expected
