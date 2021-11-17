# Monopoly

CLAMADIEU-THARAUD Adrien

QUESNOY Théo

FALLOUS Lucas

## Présentation du projet

Pré-requis : Avoir Python 3, , installer le paquet colored `pip install colored`

Ceci est un Monopoly réalisé lors du YDAY Algo et jeux de société

Nous avons créer un monopoly avec les règles de base mais nous avons modifiés les cartes chance ainsi que des rajouts de cases comme la case "Attente" ou encore "Mini-jeu". (pour plus d'informations, voir rules.md)
La case "Attente" n'a rien de spécial, c'est juste une case où il ne se passe rien.
La case "Mini-jeu" permet à deux joueurs de s'affronter dans une liste de mini-jeux (pendu, le jeu des bâtons, morpion, puissance 4)

Pour lancer le jeu il faut exécuter le main.py.
Ceci affichera un menu pour sélectionner le nombre de joueurs et leur nom, ainsi que la ou les condition(s) de victoire.
Une fois fait, le jeu commencera sur le terminal.

Le main.py s'occupe du déroulement du jeu (tour de quel joueur, les effets des cases).
Quant à l'engine.py, il initialise le plateau et contient les fonctions primaires du jeu (deplacement, lancer les dés, achat de propriétés, condition(s) de victoire...). Il est relié au fichier consoles.py qui lui s'occupe de l'affiche du jeu et permet la relation entre le jeu et l'affichage.

Pour plus de clarté et de compréhension de code, nous avons mis les différentes classes du jeu dans un dossier qui leur sont dédiés.
Les classes de jeu ont chacune une fonctionnalité propre à elle-même. Une va s'occuper de gérer ce qu'il se passe quand on tombe sur une case Mini-jeux (CaseMiniJeux.py) ou encore une autre va s'occuper que des cartes chances (Chance.py)....
