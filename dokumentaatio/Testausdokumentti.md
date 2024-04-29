# Testidokumentti

Ohjalmassa on kolmen laisia testejä. Doubly linked list on monimutkainen metodi joten se on testattu perinpohjaisesti.
Ydin algoritmit on testattu kahdesti. Ensin riisutussa ympäristössä ja sitten ns. tarkoitetussa ympäristössä.


## Testikattavuus
![Alt text](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/dokumentaatio/images/test_coverage.png)
Testikattavuusraportista on jätetty pois draw_functions kansio josta löytyy "ui", sekä services/algorithm_handler.py tiedosto.
Tämä tiedosto on vastuussa yhden algoritmin piirtämisestä (path ja point map) sekä tulosten printtaamisesta konsoliin.

## Testisyötteet
Doubly linked listin testisyötteet ovat yksiselitteisiä. Sen toiminta on selitetty hyvin [täällä](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf) joten testeilla varmistetaan että olio toimii niin.

### Moving ai labs testis
![file](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/algorithm_base_test.py)

