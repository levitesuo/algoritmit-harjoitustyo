# Käyttöohje

## Asennus

```bash
$ git clone https://github.com/levitesuo/algoritmit-harjoitusty-.git
$ cd algoritmit-harjoitusty-/
$ poetry install
```

## Ohjelman suoritus

Suorita **algoritmit-harjoitusty-/** kansiossa.

```bash
$ poetry run invoke start
```

## Syötteet

### Dataresolution

|  	|  	|
|---	|---	|
| Formaatti 	| Annan positiivinen kokonaisluku. 	|
| Kuvaus 	| Määrittää generoitavan kartan koon. Kartta generoidaan kokoon dataresolution x dataresolution.Vaikuttaa suuresti ohjelman suorituksen vaativaan aikaan. 	|
| Oletusarvo 	| 75 	|

### Random seed

|  	|  	|
|---	|---	|
| Formaatti 	| Annan positiivinen kokonaisluku. 	|
| Kuvaus 	| Määrittää siemenen josta kaikki satunnaisuus ohjelmassa arvotaa. Käytännöllinen jos halutaan tutkia samaa tilannetta useasti. 	|
| Oletusarvo 	| Satunnainen luku väliltä 1, 1000. 	|

### Start and Goal

|  	|  	|
|---	|---	|
| Formaatti 	| Kaksi positiivista kokonaislukua välillä 0 - dataresolution eroteltuna pilkulla ja välilyönnillä. 	|
| Kuvaus 	| Määrittää lähtö ja maali koordinaatit. 	|
| Oletusarvo 	| random seed sidonnainen satunnaislukupari. 	|

### Octaves

|  	|  	|
|---	|---	|
| Formaatti 	| Positiivisten liukulukujen lista eroteltuna pilkuilla ja välilyönneillä. Listan pituuden pitää olla sama kun Amplitudes listan. 	|
| Kuvaus 	| Listan pituus kertoo kuinka monta eri perlin noisea kerrostetaan päällekkäin. Arvot kertovan kyseisten äänten Oktaavit. Mitä suurempi oktaavi sitä lähempänä satunnaisuutta ääni on. Pieni oktaavi niin satunnaisuus on todella ns. pehmeää. 	|
| Oletusarvo 	| 1, 5, 10 	|

### Amplitudes

|  	|  	|
|---	|---	|
| Formaatti 	| Positiivisten liukulukujen lista eroteltuna pilkuilla ja välilyönneillä. Listan pituuden pitää olla sama kun Octaves listan. 	|
| Kuvaus 	| Listan määrittelee octaves:issa määriteltyjen äänien amplitude.  Eli ääni generoitu octaves listan ensimmäisesstä luvusta kerrotaan amplitudes listan ensimmäisellä luvulla jne. 	|
| Oletusarvo 	| 1, 0.2, 0.05 	|

### Totuusarvo syötteet

|  	|  	|
|---	|---	|
| Formaatti 	| Päällä tai pois 	|
| Kuvaus 	| Määräävät tehdäänkö jotain. 	|
| Oletusarvo 	| Päällä 	|


### Testien suorittamis komentoja

Suorittaa testit mutta ohittaa performance testauksen.
```bash
$ poetry run invoke test-skip-p
```

Suorittaa vain performance testin ja printtaa ajan konsoliin.
```bash
$ poetry run invoke performance
```

Suorittaa kaikki testit käyttäen coveragea.
```bash
$ poetry run invoke coverage
```

Suorittaa kaikki testit coveragella ja luo coverage raportin.
```bash
$ poetry run invoke coverage-report
```