---
sidebar_position: 1
---

# Intro

### Qu'est-ce que le livecoding ?

* Une performance artistique basée sur la programmation interactive de musique, visuels ou autre.

Ou comme l'exprime le manifeste de TOPLAP, un collectif à l'origine de la scène `algorave`:

>“Live Coding is a new direction in electronic music and video, and is getting somewhere interesting. Live Coders exposes and rewire the innards of software while it generates improvised music.” - toplap.org

* L'utilisation du code pour exprimer les règles génératives d'une création.
* Une forme d'écriture de musique / composition live en tant que performance
* Contrairement à la programmation classique, le code peut être changé et réexecuté en temps réel pendant que le programme tourne (pour faire évoluer la musique)
* Cette pratique transporte un langage informatique dans un environnement social et artistique et donc fait de la programmation une activité sociale à partager.

![Docusaurus logo](/img/foxdot_workshop_1.jpg)

> Un concert de livecoding (le groupe crashserver en performance au molodoï à Strasbourg)


### Pourquoi utiliser du code pour composer de la musique 

* Première on peut remarquer que l'écriture classique de la musique sur papier est déjà une sorte de code pour décrire une pièce musicale.

* Avec le livecoding il est possible:
  * de décrire des règles de composition de façon très flexible
  * décrire rapidement des choses complexes avec le clavier plutôt qu'en cliquant sur les boutons d'une interface (avec un poil d'habitude c'est beaucoup plus fluide)
  * interagir avec la composition pendant qu'elle se déroule et donc opérer de façon précise pendant une performance live

![Docusaurus logo](/img/foxdot_workshop_2.jpg)


### 1.3. What is FoxDot? 

* FoxDot a été développé par Ryan Kirkbride à Leeds UK
* FoxDot is a Python package that comes with its own IDE and plays music by accessing any SynthDefs stored on a local SuperCollider server with some custom bits of syntax to boot.
* FoxDot est une librairie (un module) en langage de programmation python pour livecoder de la musique. Il s'installe avec son propre éditeur de code (facultatif). FoxDot joue de la musique en utilisant des synthétiseurs (SynthDefs) du logiciel SuperCollider.
* Python est un langage de programmation très répendu et fait notamment pour être facilement accessible aux débutant.
* SuperCollider est un synthétiseur et langage de programmation pour la synthèse sonore et la composition algorithmique créé au départ par James McCartney en 1996.
* FoxDot se concentre sur la composition utilisant des motifs musicaux plutôt que sur la synthèse sonore qui est laissée à SuperCollider (controlé via OpenSoundControl).


#### Un petit diagramme pour donner une vision d'ensemble (pas de stress ça fonctionne même sans comprendre tout ça) :

![Docusaurus logo](/img/foxdot_workshop_3.jpg)

En mode plus technique: 

  - FoxDot is a python library, which can be used in own Python projects, or via Tkinter IDE.
  - It is also possible to configure other IDE’s to work with FoxDotn.
  - The music-making objects can be schedule events, like Timing, States, and Patterns.
  - SuperCollider provides SynthDefs (Instruments/FXs) and PBinds (Patterns/Sequences), that can be addressed and managed via OSC.