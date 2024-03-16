# Tira harjoitustyö
Leevi Suotula opinto-ohjelma: TKT
## Kielitaito
Ajattlin kirjoittaa projektin pythonissa, mutta uskon pystyväni vertaisarvioimaan myös c++ projekteja ja auttavasti Haskel projekteja.

## Määrittely
Käytetään perlin noisea generoimaan 3d korkeus kartta.
Haluaisin yrittää vertailla pathfinding algoritmeja tällä kartalla pienellä twistillä.
Haluaisin löytää ns. energiatehokkaimman reitin paikasta a paikkaan b.
Ylämäkeen liikkuminen kuluttaa energiaa jne.
Tämä idea tuli vaellusreittien suunnittelusta lapin tunturissa missä yksi reitinsuunnittelun ideoista on ettei ylämäkeen kannata nousta turhaan.

## [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise)
Perlin noisella saan generoitua uskottavia 3d maaston korkeus karttoja.
Kartat ovat käytännössä vain mustavalko kuvia joissa tummempi pikseli tarkoitta "korkeampaa" maastonkohtaa.
Voimme määritellä jonkun funktion f joka määrittää vektorin pituuden kun liikumma vaaleammasta ruudusta tummempaan jne.
Mietin vielä miten tämä funktio toteutetaan. Pitää testailla miten saa miellyttävimmät tulokset kun reitinhakualgoritmit ovat kirjoitettu. 

## Projektin ydin
Tarkoituksena olisi vertailla A* algoritmia ja Weighted Jump-Point Search algoritmia (WJPS) jota kuvaillaan tässä [artikkelissa](https://people.eng.unimelb.edu.au/pstuckey/papers/wjps.pdf). Uskon että tämä on tarpeeksi kurssin vaatimuksiin, mutta jos aikaa riittää haluaisin yrittää WJPS:n optimointeja mistä [arikkeli](https://people.eng.unimelb.edu.au/pstuckey/papers/wjps.pdf) kertoo.