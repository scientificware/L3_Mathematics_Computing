# Crible d'Eratosthène.

# Saisie de la valeur maximale des nombres premiers supérieurs à 2.
n = 0
while n <2 :
    n = int(input("Valeur maximale des nombres premiers supérieurs à 2, n = "))

# Création de la liste des nombres compris entre 2 et n.
l = [i for i in range(2,n+1)]

# Suppression des multiples de chaque nombre compris dans la première moitié de la liste.
print("Liste des valeurs supprimées à chaque itération :")
for i in range(2,int(n**0.5)+1) :
    s = 2*i
    print("sup", end=" ")
    while s <= n :
        print(s, end=" ")
        l[s-2] = ' '
        s = s + i
    print()

# Suppression des blancs.
for k in range(1,l.count(' ')+1) :
        l.remove(' ')

# Affichage des nombres premiers par dizaine.
print("Liste, par dizaine, des nombres premiers compris entre 1 et",n)
compt = 11
for i in range(len(l)) :
    # Retour à la ligne à chaque début d'une dizaine.
    if compt <= l[i] :
        print()
        compt = (l[i]//10 + 1)*10
    print(l[i], end=" ")
