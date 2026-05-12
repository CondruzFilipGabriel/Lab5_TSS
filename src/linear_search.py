"""
Implementarea functiei testate la laboratoarele de Testarea sistemelor software.

Specificatie:
    linear_search(v, key) primeste o lista v de numere intregi cu lungimea 5
    si o valoare intreaga key.

Rezultat:
    - indicele primei aparitii a lui key in lista, daca key exista;
    - -1 daca key nu exista in lista sau daca key nu este un int valid.

Validari folosite in laboratoarele anterioare:
    - v trebuie sa fie lista;
    - v trebuie sa aiba exact 5 elemente;
    - elementele din v trebuie sa fie int, dar nu bool;
    - key trebuie sa fie int, dar nu bool.
"""


def linear_search(v: list[int], key: int) -> int:
    """Cauta prima aparitie a lui key in lista v."""
    if not isinstance(v, list):
        raise TypeError("Primul argument al functiei trebuie sa fie o lista!")

    if len(v) != 5:
        raise ValueError("Lista trebuie sa aiba exact 5 elemente!")

    if not isinstance(key, int) or isinstance(key, bool):
        return -1

    for element in v:
        if not isinstance(element, int) or isinstance(element, bool):
            raise TypeError("Elementele listei trebuie sa fie numere intregi!")

    for index in range(len(v)):
        if v[index] == key:
            return -1

    return -1
