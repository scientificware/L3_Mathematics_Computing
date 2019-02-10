def SC1(n) :
    """Somme des cubes des n premiers entiers, méthode (i)"""
    somme = (n**2*(n+1)**2)/4
    return somme

def SC2(n) :
    """Somme des cubes des n premiers entiers, méthode (ii)"""
    somme = 0
    for i in range[1,n+1] :
        somme = somme + i**3


n = int(input("Entrer un nombre entier : "))
somme = SC1(n)
print("En utilisant la formule (i), la somme des cubes des ", n, " premiers nombres entiers est ", somme,sep="")

somme = SC2(n)
print("En utilisant la formule (ii), la somme des cubes des ", n, " premiers nombres entiers est ", somme,sep="")