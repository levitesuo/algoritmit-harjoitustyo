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
algorithm_base_test.py
Tässä tiedostossa testataan kaikki kolme algoritmia movingai kartassa ![AR0022SR](https://movingai.com/benchmarks/bgmaps/AR0022SR.png). Luokkaan on ohjelmoitu valmiiksi 150 eri syötettä jota voidaan kaikkia tarvittaessa testata.

Muuttuja num_of_test_cases hallitsee kuinka monta näistä syötteistä käytetään.
150 testi juokseminen vie paljon aikaa. Täten sitä kannattaa vähän rajoittaa.

Näiden testejen tarkoitus on varmistua algoritmejen oikeellisuudesta, jotta voimme käyttää myöhemmin käyttää dijkstra algoritmia toteamaan fringe_searchin ja a_starin oikeellisuus.

### Itse generoitujen karttojen testis
