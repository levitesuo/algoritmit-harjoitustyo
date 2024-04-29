# Testidokumentti

Ohjalmassa on kolmen laisia testejä. Doubly linked list on monimutkainen metodi joten se on testattu perinpohjaisesti.
Ydin algoritmit on testattu kahdesti. Ensin riisutussa ympäristössä ja sitten ns. tarkoitetussa ympäristössä.


## Testikattavuus
![Alt text](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/dokumentaatio/images/test_coverage.png)
Testikattavuusraportista on jätetty pois draw_functions kansio josta löytyy "ui", sekä services/algorithm_handler.py tiedosto.
Tämä tiedosto on vastuussa yhden algoritmin piirtämisestä (path ja point map) sekä tulosten printtaamisesta konsoliin.

## Testisyötteet
[linked_list_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/linked_list_test.py)

Doubly linked listin testisyötteet ovat yksiselitteisiä. Sen toiminta on selitetty hyvin [täällä](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf) joten testeilla varmistetaan että olio toimii niin.

### Moving ai labs testis
[algorithm_base_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/algorithm_base_test.py)

Tässä tiedostossa testataan kaikki kolme algoritmia movingai kartassa [AR0022SR](https://movingai.com/benchmarks/bgmaps/AR0022SR.png). Luokkaan on ohjelmoitu valmiiksi 150 eri syötettä jota voidaan kaikkia tarvittaessa testata. Kartan koko on 64x64 eli nodeja on 4096

Muuttuja num_of_test_cases hallitsee kuinka monta näistä syötteistä käytetään.
150 testi juokseminen vie paljon aikaa. Täten sitä kannattaa vähän rajoittaa.

Näiden testejen tarkoitus on varmistua algoritmejen oikeellisuudesta, jotta voimme käyttää myöhemmin käyttää dijkstra algoritmia toteamaan fringe_searchin ja a_starin oikeellisuus ns. tarkoitetussa ympäristössä.

### Itse generoitujen karttojen testis
[algorithm_advanced_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/algorithm_advanced_test.py)

Tässä tiedostossa testataan fringe_search sekä a_star algoritmejä itse generoiduissa kartoissa. Näit tulee samalla testattua koko ohjelman toiminnallisuus. a_starin ja fringe searchin syötteitä vertaillaan dijkstran syötteisiin samassa ympäristössä.

Luokasta löytyy tuttuun tapaa num_of_test_cases muuttuja jolla voi vaikutaa testien määrään. Samaan tapaan kuin äskön. Tämä on olemassa jotta testien suorittamiseen käytettyyn aikaan voi vaikuttaa. Tämän muuttujan voi kuitenkin halutessaan asettaa mielivaltaisen suureksi.

Kartat luodaan siemennetyllä satunnaisuudella tarkoittaen että ännäs testikartta on joka kerta testejä suorittaessa sama.

Testit juostaan eri kartoissa, mutta lähtö ja maalipisteet ovat samat. Syötteiden dataresoluutio on asetettu 50 jottei ne olisi liian raskaita. Tämä tekee testikarttojen kooksi 2500 nodea. Kyseisissä kartoissa on myös käytetty hieman eri octaves ja amplitude muuttujia kuin ohjelmassa muutoin käytetään. Karttoihin käytännössä lisättiin yksi kerron ääntä lisää. Tämä tekee kartoista vaikeampia navigoida, mutta myös ikävämmän näköisiä. Tämän takia testeissä käytetään eri muuttujaa kun ohjelmassa muuten.

Testien kartoja ja oikeita reittijä voi tarkastella suorittamalla seuraavan komennon ja antamalla sen kartan minkä haluaa nähdä.
```bash
poetry run invoke showmap
```