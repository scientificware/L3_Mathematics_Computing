un=0
n=0
while un < 1000 :
    if n == 0 :
        un = 2
    else :
       if n == 1 :
           un1 = un
           un = 1
       else :
           un2 = un1
           un1 = un
           un = 5 * un1 - 2 * un2
    print ("U(",n,")=",un)
    n = n + 1

