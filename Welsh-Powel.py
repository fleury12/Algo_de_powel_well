
## IMPORTATIONS
# N'importons de numpy que ce dont nous avons rÃ©ellement besoin !
from numpy import zeros


G = [[0, 9, 75, 2, 6,79],
     [9, 0, 95, 19, 42,5],
     [75,95, 0, 51, 66,31],
     [2, 19, 51, 0, 31,12],
     [6, 42, 66, 31, 0,37],
     [79, 5, 31, 12, 37,0]]
S=6 #le nombre de sommets
def WP(n,M):
    
    # INITIALISATION DE LA LISTE DES DEGRES
    D = []
    # CONSTRUCTION DE LA LISTE DES DEGRES
    for i in range(n):
        d = 0
        # On balaie chaque ligne de la matrice d'adjacence
        for j in range(n):
            # Si un coefficient de la ligne est non nul, on incrÃ©mente d
            if M[i][j] != 0:
                d += 1
        D.append([i,d])
    
    # TRI DE LA LISTE DES DEGRES (DANS L'ORDRE DECROISSANT)
    D.sort(key=lambda degre: degre[1])
    D.reverse()
    print(D)
    # COLORATION
    # Initialisation de l'indice des couleurs
    C = 0
    # Initialisation du nombre de sommets coloriés
    ColoredVertices = 0
    # Boucle principale : on balaie D tant qu'il reste au moins un sommet Ã ...
    # colorier !
    while ColoredVertices < len(D):
        for i in range(len(D)):
            # On ne s'intéresse qu'aux sommets non encore coloriés
            if len(D[i]) == 2:
                # Le sommet est potentiellement coloriable dans la couleur
                # courante
                ColPoss = True
                # Pour tous les sommets prÃ©cÃ©dant le sommet courant dans la
                # liste D...
                for j in range(i):
                    # Si le sommet d'indice j<i dans D est déja  colorié avec la
                    # couleur C et adjacent au sommet d'indice i dans D alors
                    # le sommet d'indice i dans D ne peut Ãªtre coloriÃ© avec C et
                    # on va passer au sommet suivant dans D sans rien faire.
                    if len(D[j]) == 3 and D[j][2] == C and M[D[i][0]][D[j][0]] >= 1:
                        ColPoss = False
                        break
                # Si on est dans une situation favorable, on colorie le sommet
                # d'indice i dans D avec la couleur courante.
                if ColPoss:
                    D[i].append(C)
                    ColoredVertices += 1
        # La liste D été balayée, on passe à  la couleur suivante...
        C +=1
    # Affichage des rÃ©sultats
    print("Nombre de couleurs utilsées :",C)
    print("Sommets ayant la même couleur :")
    for i in range(C):
        s = "couleur " + str(i) + " : "
        for e in D:
            if e[2] == i:
                s += str(e[0]) + " "
        print(s)

WP(S,G)