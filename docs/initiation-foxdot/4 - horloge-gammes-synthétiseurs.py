---
sidebar_position: 2
---

# 2 - Jouer des notes avec un synthétiseur


Au

`p1 >> pluck(0)`

# Or a list of notes

p1 >> pluck([0, 1, 2])

# Mais vous aurez besoin de spécifier tout ce que vous voulez changer...

# Comme la durée des notes, ou la longueur de chaque note.
p1 >> pluck([0, 0, 0], dur=[1, 2, 3])

# Ou l'amplitude, le "volume" de chaque note.
p1 >> pluck([0, 0, 0], amp=[1, 2, 3])

# Si la deuxième liste, l'amplitude dans cet exemple, est trop longue, alors la première liste (le degré) fait simplement une boucle, et sont appariés avec les éléments restants de la deuxième liste (l'amplitude).
p1 >> pluck([0, 2, 4], amp=[1, 2, 3, 1, 5])

# Plus généralement, toutes les listes sont parcourues quelle que soit leur longueur.
p1 >> pluck([0, 2, 4], dur=[1, 2], amp=[1, 2, 3, 1, 5])

# Les arguments peuvent être des entiers, des nombres à virgule (floats), des fractions, des listes,
# des tuples, ou un mélange

p1 >> pluck([0, 0, 0], dur=2)

p1 >> pluck([0, 0, 0], dur=1.743)

p1 >> pluck([0, 0, 0], dur=[0.25, 0.5, 0.75])

p1 >> pluck([0, 0, 0], dur=[1/4, 1/2, 3/4])

p1 >> pluck([0, 0, 0], dur=[1/4, 0.25, 3])

# Les listes de valeurs sont itérées au fur et à mesure que le joueur joue des notes.
# La durée suivante équivaut à :  1,2,3,1,4,3
# Si vous ne comprenez pas encore tout cela, ne vous inquiétez pas, vous en saurez plus sur les motifs dans le tutoriel sur les motifs.
p1 >> pluck([0, 0, 0], dur=[1, [2, 4], 3])

# Les valeurs des tuples sont utilisées simultanément, c'est-à-dire que p1 jouera 3 notes individuelles, puis un accord de 3 notes ensemble en même temps.
p1 >> pluck([0, 2, 4, (0, 2, 4)])

# Vous pouvez également attribuer directement des valeurs aux attributs des objets du lecteur.
p1.oct = 5

# Pour voir tous les noms des attributs des joueurs, il suffit d'exécuter
print(Player.get_attributes())

# Nous en reparlerons plus tard dans le tutoriel sur les attributs du joueur.

# Vous pourriez stocker plusieurs instances de lecteur et les assigner à des moments différents.
proxy_1 = pads([0, 1, 2, 3], dur=1/2)
proxy_2 = pads([4, 5, 6, 7], dur=1)

p1 >> proxy_1  # Assignez le premier à p1

p1 >> proxy_2  # Cela remplace les instructions suivies par p1

# Pour jouer plusieurs séquences à la fois, il suffit de faire la même chose avec une autre séquence.
# Objet Player :

p1 >> pluck([0, 2, 3, 4], dur=1/2)

p2 >> pads([(0, 2, 4), (3, 5, 7)], dur=8)

# Ne jouer que ce joueur, en mettant les autres en sourdine
p1.solo()  # la valeur par défaut est 1 (solo on)

# Et arrêter le solo
p1.solo(0)

# Arrêtez (et non pas seulement coupez le son) des autres joueurs.
p1.only()

# Utilisez Ctrl+. pour tout effacer pour l'horloge de programmation ou l'exécution.
Clock.clear()