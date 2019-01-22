# Affichage des termes strictement inférieurs à 1000 de la suite numérique uₙ=5×Uₙ₋₁-2×Uₙ₋₂.
# Initialisation des variables.
un=0
n=0
while un < 1000 :
    if n > 1 :
	# Met à jour les termes de rang n-1 et n-2
        un2 = un1
        un1 = un
        un = 5 * un1 - 2 * un2
    else :
	# Initialise le premier terme.
        if n == 0 :
            un = 2
        else :
            # Initialise les deux premiers termes.
            if n == 1 :
                un1 = un
                un = 1
    print ("U(",n,")=",un)
    n = n + 1
