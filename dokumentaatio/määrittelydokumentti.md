Leevi Suotula opinto-ohjelma: TKT
## Kielitaito
Ajattlin kirjoittaa projektin pythonissa, mutta uskon pystyväni vertaisarvioimaan myös c++ projekteja ja auttavasti Haskel projekteja.

## Määrittely
Tarkoituksena on vertailla a*, fringe search sekä dijkstra algoritmeja mielenkiintoisessa ympäristössä.
Vektori kartat näille algoritmeille on tehthy mallintamaan "energiatehokkaimman" reitin löytämiseksi 3d ympäristössä.
Ajatus tuli vaellusreitin suunnittelusta, missä halutaan välttää suurien mäkien yli menemistä vaan mennään mielummin niiden  ympäri.

## [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise)
Perlin noisella saan generoitua uskottavia 3d maaston korkeus karttoja.
Kartat ovat käytännössä vain mustavalko kuvia joissa tummempi pikseli tarkoitta "korkeampaa" maastonkohtaa.
Voimme määritellä jonkun funktion f joka määrittää vektorin pituuden kun liikumma vaaleammasta ruudusta tummempaan jne.
Tämä funktio f löytyy kohdasta height mapping function.

## Projektin ydin
Tarkoituksena olisi vertailla A* algoritmia ja Fringe search algoritmia jota kuvaillaan tässä [artikkelissa](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf). 