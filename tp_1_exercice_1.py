x=int(input("Entrer le premier opérande : "))
y=int(input("Entrer le second opérande : "))

resultat = x + y
print ( x , "+" , y , "=" , resultat)

resultat = x - y
print ( x , "-" , y , "=", resultat)

resultat = x*y
print ( x , "×" , y , "=", resultat)

if y==0 :
    if x==0 :
        print ("L'opération 0 ÷ 0 donne une infinité de valeurs")
    else :
        print ("L'opération",x,"÷ 0 n'est pas définie")
else :
    resultat = x/y
    print ( x, "÷" , y , "=" , resultat)
