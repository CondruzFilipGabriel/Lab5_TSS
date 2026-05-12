# Raport scurt - Laborator L5 CI/CD

Pentru laboratorul L5 a fost configurat un pipeline CI/CD folosind GitHub Actions. Pipeline-ul ruleaza automat la fiecare push pe branch-ul `main` si verifica proiectul Python implementat pentru functia `linear_search(v, key)`. Verificarile includ rularea tuturor testelor automate, generarea raportului de coverage, aplicarea unui prag minim de coverage de 80% (<b>ci.yml</b>: `python3 -m coverage report -m --fail-under=80`) si rularea mutation testing cu `mutmut`.

## Timpul de rulare al pipeline-ului

Pipeline-ul complet a durat aproximativ 58 de secunde la prima rulare reusita si aproximativ 52 de secunde dupa repararea bug-ului introdus intentionat. Jobul de teste si coverage a durat aproximativ 16-19 secunde, iar jobul de mutation testing aproximativ 26-28 de secunde.

In cazul rularii esuate, pipeline-ul s-a oprit dupa aproximativ 24 de secunde, deoarece jobul `Tests and coverage` a esuat. Jobul `Mutation testing` nu a mai fost executat, deoarece depinde de succesul testelor initiale.

## Ce se intampla daca un coleg face push cu un test nou care pica?

Daca un coleg face push cu un test nou care pica, pipeline-ul este marcat automat ca esuat. Jobul `Tests and coverage` se opreste cu eroare, iar GitHub Actions afiseaza rularea cu status rosu. In acest caz, codul nu mai este considerat valid din punctul de vedere al verificarilor automate.

De asemenea, workflow-ul creeaza automat o notificare sub forma unui GitHub Issue. Issue-ul contine repository-ul, branch-ul, commit-ul, autorul push-ului si linkul catre rularea esuata. Astfel, problema poate fi identificata rapid fara verificare manuala permanenta.

## Avantajele fata de rularea manuala a testelor

Abordarea CI/CD are avantajul ca testele sunt rulate automat la fiecare modificare a codului. Nu mai este necesar ca fiecare dezvoltator sa isi aminteasca sa ruleze manual toate comenzile de testare, coverage si mutation testing. Astfel, scade riscul ca un bug sa fie introdus in repository fara sa fie observat.

Un alt avantaj este reproductibilitatea. Pipeline-ul ruleaza intr-un mediu controlat, folosind aceleasi comenzi si aceleasi dependinte de fiecare data. Rezultatele sunt vizibile in GitHub Actions si pot fi verificate ulterior.

In plus, rapoartele de coverage si rezultatele mutation testing sunt salvate ca artefacte descarcabile. Acest lucru permite analiza ulterioara a calitatii suitei de teste. Pragul minim de coverage impiedica acceptarea unor modificari care reduc acoperirea sub nivelul stabilit.

Prin urmare, CI/CD aduce automatizare, trasabilitate, verificare constanta si siguranta mai mare fata de rularea manuala a testelor.