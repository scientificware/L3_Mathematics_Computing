# Liste des nombres d'Armstrong compris entre 0 et 999
print("Liste des nombres d'Armstrong compris entre 0 et 999")
for c in range(0,9,1) :
    for d in range(0,9,1) :
        for u in range(0,9,1) :
            n = c*100+d*10+u
            if n == c**3 + d**3 + u**3 :
                print(n,"=",c,"³+",d,"³+",u,"³")