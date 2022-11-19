---
sidebar_position: 1
---

# Intro

Ce support est sous licence `CC-BY-SA`. Il est partiellement une traduction du tutoriel FoxDot (in app), du cours de iShapeNoise/BBScar ici `https://gitlab.com/iShapeNoise/foxdot_codingmusic_part1` et un travail original.

Un grand merci à BBScar, Qirky et les contributeurs de FoxDot, pour l'existence de ce logiciel fascinant et sa communauté.

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


### 1.3. Qu'est ce que FoxDot? 

FoxDot est un outil qui simplifie la génération de musique via le code. Le projet est inspiré et basé sur SuperCollider. En effet SuperCollider est un logiciel de synthèse sonore et de composition algorithmique extrêment puissant et flexible mais complexe à aborder. Il nécessite une quantité assez importante de code pour générer de la musique.

* FoxDot est une bibliothèque (library, une sorte de module à importer) en langage de programmation Python pour livecoder de la musique. Il s'installe avec son propre éditeur de code (facultatif).

* FoxDot a été développé par Ryan Kirkbride à Leeds (UK) 

* FoxDot joue de la musique en utilisant des synthétiseurs (SynthDefs) présent dans SuperCollider(controlé via OpenSoundControl).

* Le Python est un langage de programmation très répandu et conçu notamment pour être facilement accessible aux débutants.

* SuperCollider est un synthétiseur et langage de programmation pour la synthèse sonore et la composition algorithmique créé au départ par James McCartney en 1996.

* FoxDot se concentre sur la composition utilisant des motifs musicaux plutôt que sur la synthèse sonore qui est laissée à SuperCollider .


#### Un petit diagramme pour donner une vision d'ensemble (pas de stress ça fonctionne même sans comprendre tout ça) :

![foxdot architecture diagram](/img/foxdot_workshop_3.jpg)

En version plus technique: 

  - FoxDot is a python library, which can be used in own Python projects, or via Tkinter IDE.
  - It is also possible to configure other IDE’s to work with FoxDotn.
  - The music-making objects can be schedule events, like Timing, States, and Patterns.
  - SuperCollider provides SynthDefs (Instruments/FXs) and PBinds (Patterns/Sequences), that can be addressed and managed via OSC.