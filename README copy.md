# Linear Search - Testarea sistemelor software

Proiect Python pentru testarea functiei `linear_search(v, key)`. Functia primeste o lista `v` cu exact 5 numere intregi si o valoare intreaga `key`. Rezultatul este indicele primei aparitii a valorii `key` in lista sau `-1` daca valoarea nu exista.

## Structura

```text
repo/
├── README.md
├── requirements.txt
├── setup.cfg
├── src/
│   └── linear_search.py
└── tests/
    ├── __init__.py
    ├── oracle.py
    ├── test_black_box.py
    ├── test_white_box.py
    └── test_random.py
```

## Suite de teste

- `test_black_box.py` contine testele functionale: partitionare de echivalenta si valori de frontiera.
- `test_white_box.py` contine testele structurale: statement coverage, decision coverage si condition coverage.
- `test_random.py` contine 1000 de cazuri generate aleatoriu cu seed fix si verificate printr-un oracol independent.

## Rulare locala

Instalarea dependentelor:

```bash
python3 -m pip install -r requirements.txt
```

Rularea tuturor testelor:

```bash
python3 -m pytest -q
```

Rularea coverage cu branch coverage:

```bash
python3 -m coverage erase
python3 -m coverage run -m pytest
python3 -m coverage report -m
python3 -m coverage html
```

Rularea mutation testing:

```bash
mutmut run
mutmut results
```

## Badge CI

Badge-ul de status va fi adaugat dupa crearea repository-ului GitHub si dupa stabilirea numelui workflow-ului. Badge-ul va arata daca ultima rulare a pipeline-ului CI a trecut sau a esuat.
