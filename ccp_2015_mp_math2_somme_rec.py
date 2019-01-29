def somme_rec(n) :
    """Somme des chiffres d'un nombre"""
    if (n==0) :
        # Initialisation de la somme
        return 0
    else :
        return ((n%10)+somme_rec(n//10))


n = int(input("Entrer un entier n > 0, sinon le programme choisira 1 : "))
n = max(1,n)
s = somme_rec(n)
print("la somme des chiffres de", n, "est", s)