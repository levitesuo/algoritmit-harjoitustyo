# Testidokumentti

Ohjalmassa on kolmen laisia testejä. Doubly linked list on monimutkainen metodi joten se on testattu perinpohjaisesti.
Ydin algoritmit on testattu kahdesti. Ensin riisutussa ympäristössä ja sitten ns. tarkoitetussa ympäristössä.


## Testikattavuus
![Alt text](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/dokumentaatio/kuvat/test_coverage.png)
Testikattavuusraportista on jätetty pois draw_functions kansio josta löytyy "ui", sekä services/algorithm_handler.py tiedosto.
Tämä tiedosto on vastuussa yhden algoritmin piirtämisestä (path ja point map) sekä tulosten printtaamisesta konsoliin.

## Testisyötteet
[linked_list_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/linked_list_test.py)

Doubly linked listin testisyötteet ovat yksiselitteisiä. Sen toiminta on selitetty hyvin [täällä](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf) joten testeilla varmistetaan että olio toimii niin.

### Moving ai labs testis
[algorithm_base_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/algorithm_base_test.py)

Tässä tiedostossa testataan kaikki kolme algoritmia movingai [kartoissa](https://movingai.com/benchmarks/bgmaps/index.html). Projektin map_generation kansiosta voi valita haluamansa kartat ja suorittaa niiden kaikki .scen tiedostossa mainitut syötteet. Tämän kanssa kuitenkin kannattaa olla varovainen sillä joidenkin karttojen syötteiden suorittamisessa saattaa mennä ikä sekä terveys.


Näiden testejen tarkoitus on varmistua algoritmejen oikeellisuudesta, jotta voimme käyttää myöhemmin dijkstra algoritmia toteamaan fringe_searchin ja a_starin oikeellisuus ns. tarkoitetussa ympäristössä.

### Itse generoitujen karttojen suorituskykytestaus
[algorithm_advanced_test.py](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/src/tests/algorithm_advanced_test.py)

Tässä tiedostossa testataan fringe_search sekä a_star algoritmejä itse generoiduissa kartoissa. Näin tulee samalla testattua koko ohjelman toiminnallisuus. a_starin ja fringe searchin syötteitä vertaillaan dijkstran syötteisiin.

Luokasta löytyy 3 muuttujaa jolla voi vaikuttaa testien vaativuuteen.
- num_of_maps
- num_of_runs_per_map
- data_resolution

Muuttujat ovat mielestni yksiselitteisiä. 

Jokaiselle ns. runille (jonka määrän voi asettaa num_of_runs_per_map muuttujalla) arvotaan seeden varainen aloitus ja lopetus paikka. Tällä voidaan varmistaa että syötteet ovat eriäviä.

Joka ikisen algoritmin suorituksen oikeutta arvioidaan vertaamalla parhaan reitin pituutta dijkstarin antamaan parhaan reitin pituuten. Algoritmeijen juoksuaikaa myös lasketaan, jonka avulla suoritetaan suorituskykytestausta.

Kuten aloitus ja lopetus kohdat kartat on luotu siemennetyllä satunnaisuudella jotta ensimmäiset n karttaa ovat aina samat.

### Huomio

Lähtökohtaisesti fringe search on marginaalisesti hitaampi kuin a_star. Sen takia sen suoritusta a_starin ei verrata testeissä automaattisesti. Testejä juoksiessa huomasin kuitenkin että tietyllä data_resoluutiolla on yleistä (ainakin pöytäkoneellani) että fringe search on hiukan nopeampi kuin a_star. Tässä vielä relevantit muuttujat tilanteeseen jonka dokumentoin [näytönkaappauksella](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/dokumentaatio/kuvat/Screenshot%20from%202024-05-03%2000-20-11.png)

#### Variables

- num_of_maps = 10
- num_of_runs_per_map = 50
- data_resolution = 50
- seed = 10

#### Results

- fringe_search_time = 32.97014403343201
- a_star_time =  34.6319019797944641
- dijkstra_time = 46.915706396102905
