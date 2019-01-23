# Calcul de la moyenne de 8 note en excluant une des valeurs maximales ou minimales s'il en existe plusieurs occurences.
l={}
lmax = 0
occ_max = -1
lmin = 0
occ_min = -1
nb = 8
somme = 0
for i in range(nb) :
    l[i] = int(input("Valeur = "))
    somme = somme + l[i]
    if occ_max == -1 :
        lmax = l[i]
        lmin = l[i]
        occ_min = 1
        occ_max = 1
    else :
        if lmin > l[i] :
            lmin = l[i]
            occ_min = 1
        else :
            if lmin == l[i] :
               occ_min = occ_min + 1
        if lmax < l[i] :
            lmax = l[i]
            occ_max = 1
        else :
            if lmax == l[i] :
                occ_max = occ_max + 1 
if occ_min > 1 :
    somme =  somme - lmin
    nb = nb - 1
    print("Une des valeurs minimales a été exclue")
if occ_max > 1 :
    somme = somme - lmax
    nb = nb -1
    print("Une des valeurs maximales a été exclue")

print("La moyenne sera calculée en utilisant",nb,"valeurs sur",8)
print("La moyenne est de :", somme/nb)

for i in range(8) :
    print("Valeur l[", i, "] = ",l[i])
