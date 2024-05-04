# Testidokumentti

Ohjelmassa lähes kaikki keskeiset funktiot on testattu niille tarkoitetuille unittesteillä. Sen lisäksi itse algoritmejä on testattu neljällä eri tavalla.

## Testikattavuus
![Alt text](https://github.com/levitesuo/algoritmit-harjoitusty-/blob/main/dokumentaatio/test_coverage_report.png)
Testikattavuusraportista on jätetty pois draw_functions, ui sekä index. Shape functions tiedostossa on erillisiä metodeita jotka on jätetty testikattavuuden ulkopuolelle, sillä niitä ei käytetä ohjelman suorituksessa.

## Erilaisia testejä

app_engine_test, linked_list_test, node_list_generator_test, translator_test ovat kaikki simplleleitä unit testejä. Niissä testataan algoritmejä tukevia metodeita.

Loput testeistä testaa algoritmejä. Jokainen tulevista testeistä suoritetaan kaikille kolmelle algoritmille.

#### algorithm_blank_3_test

Testit tässä tiedostossa tapahtuu 3x3 tyhjällä 2d kartalla. Tällä kartalla testataan muutamia tilanteita ja tarkistetaan että algoritmejen reitit ovat oikeaita ja että algoritmejen käydyt solut ovat tarkoituksenmukaisia.

#### algorithm_dot_3_test

Testit itsessään on samanlaisia kuin blank_3 testit, mutta kartta on 3x3 ruutu jossa on läpipääsemätön seinä keskellä.

#### algorithm_validity_test

Varmistuaksemme algoritmejen oikeellisuudesta tässä tiedostossa testataan algoritmejä movingai kartoissa pelistä bouldersgate 2. Tiedoston avulla voimme suoritaa kaikki tilanteet jotka löytyvät map_generation/maps kansiosta. Olen suorittanut kotikoneella enemmänkin testejä, mutta oletukseksi on jätetty nopeite suoritettavissa oleva datasetti.

Nämä testit suoritetaan oikeestaan että voidaan olla aivan varmoja djikstran oikeellisuudesta, jotta tulevissa testeissä voidaan pitää sen syötteitä erilaisilla kartoilla vertailukohtana.

```mermaid
sequenceDiagram title Algoritmin suoritus validity testeissä
  actor Tester
  participant node_list_generator
  participant two_d_translator
  participant algorithm
  Tester->>node_list_generator:node_list_generator((filepath.map).read(), True)
  node_list_generator->>Tester:node_list
  Tester->>two_d_translator:two_d_translator(start, goal, node_list, arg)
  two_d_translator->>two_d_translator:translates start and goal
  two_d_translator->>algorithm:algorithm(args)
  algorithm->>two_d_translator:results
  two_d_translator->>Tester:results
```


#### algorithm_performance_test

Täällä suoritetaan testejä itse generoiduissa kartoissa. Tiedoston nimen mukaan juoksemme performance testejä mitaten aikaa. Fringe searchin performancea ei vertailla suoraan unittestillä sillä se on huomattavasti hitaampi kuin djikstra ja a_star. Testejen aikana varmistetaan kuitenkin että a_starin ja fringe_searchin tulosteet vastaavat djikstran tulostetta, jonka oletamme oikeaksi. Isoimmat suoritetut testimäärät tällä testillä on sample size 500 tilannetta joissa jokaisessa 2500 nodea.

#### integration_test

Täällä kutsutaan suoraan AppEngine luokkaa josta käsin suoritetaan kaikki algoritmit eri satunnaisella siemenellä, ja varmistetaan että niiden reittien pituudet ovat lyhyimmät mahdolliset.

```mermaid
sequenceDiagram title Algoritmin suoritus integraatio testeissä
  actor Tester
  participant app_service
  participant get_shape
  participant node_list_generator
  participant algorithm_handler
  participant translator
  participant algorithm
  participant drawing_funcs
  Tester->> app_service: execute()
  app_service->>get_shape:get_shape(layered_noise(args))
  get_shape->>app_service:grid
  app_service->>node_list_generator:node_list_generator(grid, False)
  node_list_generator->>app_service:node_list
  app_service->>drawing_funcs:draw a plain
  app_service->>algorithm_handler:algorithm_handler(start, goal, node_list, args)
  algorithm_handler->>translator:translator(start, goal, node_list, args)
  translator->>translator:Translates goal and start
  translator->>algorithm:algorithm(args)
  algorithm->>translator:results
  translator->>translator:translates path, measures time
  translator->>algorithm_handler: results + results['time']
  algorithm_handler->>app_service: results
  app_service->>Tester:results


```