"""Oracol independent pentru testele random."""


def oracle_linear_search(v: list[int], key: int) -> int:
    """
    Returneaza rezultatul asteptat fara sa apeleze functia testata.

    Implementarea foloseste metoda list.index si trateaza explicit cazul in care
    cheia nu exista in lista.
    """
    try:
        return v.index(key)
    except ValueError:
        return -1
