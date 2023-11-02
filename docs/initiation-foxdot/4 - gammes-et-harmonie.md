---
title: Changez le tempo et la gamme
sidebar_position: 5
---


## 2 Horloge (Clock) de FoxDot

Les boucles/patterns dans FoxDot sont dépendants du temps qui s'écoule (comme toute musique). La `Clock` est l'objet responsable de compter l'écoulement des temps ou beats dans FoxDot. Tous les players (p1,a3,x7...) auxquels on assigne des synthés et patterns à jouer sont reliés à (ou programmés sur) cette horloge commune ce qui leur permet d'être tous synchronisés.

Il est intéressant de savoir manipuler un peu l'horloge pour :

- changer la vitesse de lecture ou bpm de la musique
- savoir désigner des points dans le futur pour déclencher des évènements musicaux plus tard
- Ajuster la synchronisation MIDI
- Savoir arrêter les joueurs ou utiliser plusieurs horloges désynchronisées (avancé)

### Changer le bpm

Par défaut le bpm de FoxDot est 120. Pour le changer on peut utiliser :

`Clock.bpm = 140`

### Désigner un point dans le futur

Utilisez `print()` sur `Clock.mod(4)`, `Clock.now()`, `Clock.mod(16)`.

Ces indications de moment dans le futur (en nombre de beat depuis l'allumage de FoxDot) servent principalement à controler les variables temporelles comme indiqué dans la partie suivante.

<!-- ### Programmer une fonction plus tard -->

<!-- On peut utiliser -->