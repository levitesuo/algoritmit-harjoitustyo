Leevi Suotula opinto-ohjelma: TKT
## Kielitaito
Ajattlin kirjoittaa projektin pythonissa, mutta uskon pystyväni vertaisarvioimaan myös c++ projekteja ja auttavasti Haskel projekteja.

## Määrittely
Vaellusreitin suunnittelu algoritmisesti.
Tämä algoritmi ikävä kyllä ottaa reitin suunnittelussa huomioon vain maaston korkeuden.
Käytetään perlin noisea generoimaan 3d korkeus kartta.
Haluaisin löytää ns. energiatehokkaimman reitin paikasta a paikkaan b.
Käytännössä ylämäkeen liikkuminen kuluttaa paljon energiaa kun taas alamäkeen ei ole sen helpompaa kulkea kun tasaisella kävely.
Aloitetaan funtiolla
liikkumisen hinta = max(1.4 ** (ylöspäin liikkeen määrä * a - 10), 0)
a = positiivinen realilukukerroin

Hypoteesina on että vaikka alaspäin liikkuminen voi olla ilmaista pitää algoritmitn

## [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise)
Perlin noisella saan generoitua uskottavia 3d maaston korkeus karttoja.
Kartat ovat käytännössä vain mustavalko kuvia joissa tummempi pikseli tarkoitta "korkeampaa" maastonkohtaa.
Voimme määritellä jonkun funktion f joka määrittää vektorin pituuden kun liikumma vaaleammasta ruudusta tummempaan jne.
Mietin vielä miten tämä funktio toteutetaan. Pitää testailla miten saa miellyttävimmät tulokset kun reitinhakualgoritmit ovat kirjoitettu. 

## Projektin ydin
Tarkoituksena olisi vertailla A* algoritmia ja Weighted Jump-Point Search algoritmia (WJPS) jota kuvaillaan tässä [artikkelissa](https://people.eng.unimelb.edu.au/pstuckey/papers/wjps.pdf). Uskon että tämä on tarpeeksi kurssin vaatimuksiin, mutta jos aikaa riittää haluaisin yrittää WJPS:n optimointeja mistä [arikkeli](https://people.eng.unimelb.edu.au/pstuckey/papers/wjps.pdf) kertoo.