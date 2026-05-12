"""
Teste structurale white-box pentru linear_search(v, key).

Suita acopera cazurile folosite anterior pentru:
    - statement coverage;
    - decision coverage;
    - condition coverage.
"""

import re

import pytest

from linear_search import linear_search


STATEMENT_COVERAGE_CASES = [
    {
        "id": "SC1",
        "v": "abc",
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "SC2",
        "v": [1, 2, 3],
        "key": 1,
        "exception": ValueError,
        "message": "Lista trebuie sa aiba exact 5 elemente!",
    },
    {
        "id": "SC3",
        "v": [1, 2, 3, 4, 5],
        "key": True,
        "expected": -1,
    },
    {
        "id": "SC4",
        "v": [1, 2, "x", 4, 5],
        "key": 4,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "SC5",
        "v": [10, 20, 30, 40, 50],
        "key": 30,
        "expected": 2,
    },
    {
        "id": "SC6",
        "v": [10, 20, 30, 40, 50],
        "key": 99,
        "expected": -1,
    },
]


DECISION_COVERAGE_CASES = [
    {
        "id": "DC1_D1_true",
        "v": "abc",
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "DC2_D2_true",
        "v": [1, 2, 3],
        "key": 1,
        "exception": ValueError,
        "message": "Lista trebuie sa aiba exact 5 elemente!",
    },
    {
        "id": "DC3_D3_true",
        "v": [1, 2, 3, 4, 5],
        "key": True,
        "expected": -1,
    },
    {
        "id": "DC4_D4_true",
        "v": [1, 2, "x", 4, 5],
        "key": 4,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "DC5_D5_true",
        "v": [10, 20, 30, 40, 50],
        "key": 30,
        "expected": 2,
    },
    {
        "id": "DC6_D5_false",
        "v": [10, 20, 30, 40, 50],
        "key": 99,
        "expected": -1,
    },
]


CONDITION_COVERAGE_CASES = [
    {
        "id": "CC1_key_non_int",
        "v": [1, 2, 3, 4, 5],
        "key": "abc",
        "expected": -1,
    },
    {
        "id": "CC2_key_bool",
        "v": [1, 2, 3, 4, 5],
        "key": True,
        "expected": -1,
    },
    {
        "id": "CC3_element_non_int",
        "v": [1, 2, "x", 4, 5],
        "key": 4,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "CC4_element_bool",
        "v": [1, 2, False, 4, 5],
        "key": 4,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "CC5_elemente_valide_key_absent",
        "v": [10, 20, 30, 40, 50],
        "key": 99,
        "expected": -1,
    },
]


def verifica_caz(case: dict) -> None:
    """Executa un caz structural si verifica rezultatul sau exceptia asteptata."""
    if case.get("exception") is not None:
        with pytest.raises(case["exception"], match=re.escape(case["message"])):
            linear_search(case["v"], case["key"])
    else:
        assert linear_search(case["v"], case["key"]) == case["expected"]


@pytest.mark.parametrize(
    "case",
    STATEMENT_COVERAGE_CASES,
    ids=lambda case: case["id"],
)
def test_statement_coverage(case):
    verifica_caz(case)


@pytest.mark.parametrize(
    "case",
    DECISION_COVERAGE_CASES,
    ids=lambda case: case["id"],
)
def test_decision_coverage(case):
    verifica_caz(case)


@pytest.mark.parametrize(
    "case",
    CONDITION_COVERAGE_CASES,
    ids=lambda case: case["id"],
)
def test_condition_coverage(case):
    verifica_caz(case)
