cat > README.md <<'EOF'
# Linear Search - Testarea Sistemelor Software

[![CI](https://github.com/CondruzFilipGabriel/Lab5_TSS/actions/workflows/ci.yml/badge.svg)](https://github.com/CondruzFilipGabriel/Lab5_TSS/actions/workflows/ci.yml)

## Descrierea proiectului

Acest repository contine proiectul realizat pentru laboratorul L5 la disciplina Testarea Sistemelor Software.

Proiectul testeaza functia `linear_search(v, key)`. Functia primeste o lista `v` de 5 numere intregi si o valoare intreaga `key`. Rezultatul este indicele primei aparitii a valorii `key` in lista. Daca valoarea nu exista in lista, functia returneaza `-1`.

Repository-ul include suitele de teste realizate la laboratoarele anterioare:

- teste black-box;
- teste white-box;
- teste random;
- oracol independent pentru testele random;
- configurare CI/CD prin GitHub Actions;
- generare automata de raport coverage;
- rulare mutation testing cu `mutmut`.

## Structura proiectului

```text
repo/
├── README.md
├── raport_l5.md
├── requirements.txt
├── setup.cfg
├── src/
│   └── linear_search.py
├── tests/
│   ├── test_black_box.py
│   ├── test_white_box.py
│   └── test_random.py
└── .github/
    └── workflows/
        └── ci.yml
```

Folderul `htmlcov/` este generat automat de `coverage.py` si nu trebuie incarcat manual in repository.

## Instructiuni de rulare locala a testelor

Pentru instalarea dependentelor:

```bash
python3 -m pip install -r requirements.txt
```

Pentru rularea tuturor testelor:

```bash
python3 -m pytest -q
```

Pentru rularea testelor cu masurarea coverage-ului:

```bash
python3 -m coverage erase
python3 -m coverage run -m pytest -q
python3 -m coverage report -m
python3 -m coverage html
```

Raportul HTML de coverage este generat in folderul:

```text
htmlcov/
```

Fisierul principal al raportului este:

```text
htmlcov/index.html
```

Pentru rularea mutation testing:

```bash
mutmut run
mutmut results
```

## Pipeline CI/CD

Pipeline-ul este configurat in fisierul:

```text
.github/workflows/ci.yml
```

Acesta ruleaza automat la fiecare push pe branch-ul `main`.

Etapele principale ale pipeline-ului sunt:

1. descarcarea codului din repository;
2. instalarea Python si a dependentelor;
3. rularea tuturor testelor;
4. generarea raportului HTML de coverage;
5. verificarea pragului minim de coverage;
6. salvarea raportului de coverage ca artefact;
7. rularea mutation testing;
8. salvarea rezultatelor mutation testing ca artefact.

Pragul minim de coverage este setat la 80% prin comanda:

```bash
python3 -m coverage report -m --fail-under=80
```

Daca acoperirea scade sub acest prag, pipeline-ul esueaza.

## Artefacte generate

Pipeline-ul genereaza doua artefacte descarcabile din pagina rularii GitHub Actions:

- `coverage-html-report` - raportul HTML generat de `coverage.py`;
- `mutation-testing-results` - rezultatele generate de `mutmut`.

## Semnificatia badge-ului CI

Badge-ul afisat la inceputul fisierului indica starea curenta a pipeline-ului CI.

Semnificatia acestuia este urmatoarea:

- `passing` / verde - ultima rulare a pipeline-ului a trecut cu succes;
- `failing` / rosu - ultima rulare a pipeline-ului a esuat;
- click pe badge - deschide pagina GitHub Actions pentru workflow-ul CI.

Badge-ul permite verificarea rapida a starii proiectului fara accesarea manuala a paginii de Actions.

## Notificare la esec

Workflow-ul este configurat sa creeze automat un GitHub Issue atunci cand pipeline-ul esueaza la un push pe branch-ul `main`.

Issue-ul generat contine:

- repository-ul;
- branch-ul;
- commit-ul;
- autorul push-ului;
- link catre rularea esuata.

Aceasta notificare permite identificarea rapida a problemelor aparute dupa un push.