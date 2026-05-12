"""
Teste functionale black-box pentru linear_search(v, key).

Suita reuneste cazurile folosite anterior pentru:
    - partitionare de echivalenta;
    - analiza valorilor de frontiera.
"""

import re

import pytest

from linear_search import linear_search


PARTITIONARE_EQUIVALENTA_CASES = [
    {
        "id": "EP1_v_nu_este_lista",
        "v": "abc",
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "EP2_lungime_invalida",
        "v": [1],
        "key": 1,
        "exception": ValueError,
        "message": "Lista trebuie sa aiba exact 5 elemente!",
    },
    {
        "id": "EP3_element_invalid",
        "v": ["a", 1, 2, 3, 4],
        "key": 1,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "EP4_key_exista",
        "v": [1, 2, 3, 4, 5],
        "key": 1,
        "expected": 0,
    },
    {
        "id": "EP5_key_nu_exista",
        "v": [1, 2, 3, 4, 5],
        "key": 0,
        "expected": -1,
    },
    {
        "id": "EP6_prima_aparitie",
        "v": [4, 7, 4, 7, 4],
        "key": 4,
        "expected": 0,
    },
]


VALORI_FRONTIERA_CASES = [
    {
        "id": "BV1_key_string",
        "v": [1, 2, 3, 4, 5],
        "key": "1",
        "expected": -1,
    },
    {
        "id": "BV2_key_bool",
        "v": [1, 2, 3, 4, 5],
        "key": True,
        "expected": -1,
    },
    {
        "id": "BV3_key_none",
        "v": [1, 2, 3, 4, 5],
        "key": None,
        "expected": -1,
    },
    {
        "id": "BV4_v_string",
        "v": "a",
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "BV5_v_int",
        "v": 1,
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "BV6_v_bool",
        "v": True,
        "key": 1,
        "exception": TypeError,
        "message": "Primul argument al functiei trebuie sa fie o lista!",
    },
    {
        "id": "BV7_lungime_sub_limita",
        "v": [1, 2, 3, 5],
        "key": 1,
        "exception": ValueError,
        "message": "Lista trebuie sa aiba exact 5 elemente!",
    },
    {
        "id": "BV8_lungime_peste_limita",
        "v": [1, 2, 3, 4, 5, 6],
        "key": 1,
        "exception": ValueError,
        "message": "Lista trebuie sa aiba exact 5 elemente!",
    },
    {
        "id": "BV9_element_bool",
        "v": [False, 1, 2, 3, 4],
        "key": 1,
        "exception": TypeError,
        "message": "Elementele listei trebuie sa fie numere intregi!",
    },
    {
        "id": "BV10_key_pe_prima_pozitie",
        "v": [1, 2, 3, 4, 5],
        "key": 1,
        "expected": 0,
    },
    {
        "id": "BV11_key_pe_ultima_pozitie",
        "v": [1, 2, 3, 4, 5],
        "key": 5,
        "expected": 4,
    },
]


def verifica_caz(case: dict) -> None:
    """Executa un caz functional si verifica rezultatul sau exceptia asteptata."""
    if case.get("exception") is not None:
        with pytest.raises(case["exception"], match=re.escape(case["message"])):
            linear_search(case["v"], case["key"])
    else:
        assert linear_search(case["v"], case["key"]) == case["expected"]


@pytest.mark.parametrize(
    "case",
    PARTITIONARE_EQUIVALENTA_CASES,
    ids=lambda case: case["id"],
)
def test_partitionare_echivalenta(case):
    verifica_caz(case)


@pytest.mark.parametrize(
    "case",
    VALORI_FRONTIERA_CASES,
    ids=lambda case: case["id"],
)
def test_valori_frontiera(case):
    verifica_caz(case)
