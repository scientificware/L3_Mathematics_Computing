# Crible d'Eratosthène.
ctlHTMLBegin = ("<!--"
                " Copyright (c) 2018. Guy Abossolo Foh. All rights reserved."
                " DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER."
                ""
                " This code is free software; you can redistribute it and/or modify it"
                " under the terms of the GNU General Public License version 2 only, as"
                " published by the Free Software Foundation."
                ""
                " This code is distributed in the hope that it will be useful, but WITHOUT"
                "  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or"
                "  FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License"
                "  version 2 for more details (a copy is included in the LICENSE file that"
                "  accompanied this code)."
                ""
                "  You should have received a copy of the GNU General Public License version"
                "  2 along with this work; if not, write to the Free Software Foundation,"
                "  Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA."
                ""
                "  Please contact Guy Abossolo Foh, 71 rue Guy de Maupassant 69500 Bron France"
                "  or visit www.scientificware.com if you need additional information or have any"
                "  questions."
                "  -->"
                "<html>"
                "  <head>"
                "    <meta charset=\"UTF-8\"/>"
                "  </head>"
                "  <body>")
ctlHTMLEnd = (  "  </body>"
                "</html>")
# Saisie de la valeur maximale des nombres premiers supérieurs à 2.
n = 0
while n <2 :
    n = int(input("Valeur maximale des nombres premiers supérieurs à 2, n = "))

# Création de la liste des nombres compris entre 2 et n.
l = [i for i in range(2,n+1)]

# Suppression des multiples de chaque nombre compris entre 2 et la racine carrée de n.
print("Liste des valeurs supprimées à chaque itération :")
for i in range(2,int(n**0.5)+1) :
    # Vérification situation d'un multiple déjà traité sinon suppression de ses multiples
    if l[i-2] != ' ' :
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

# Affichage des nombres premiers par centaine.
print("")
print("Liste, par centaine, des nombres premiers compris entre 1 et",n)
compt = 101

print(ctlHTMLBegin,"<table>",end="<tr>")
for i in range(len(l)) :
    # Retour à la ligne à chaque début d'une centaine.
    if compt <= l[i] :
        print("</tr>")
        compt = (l[i]//100 + 1)*100
    print("<td>", str(l[i]), sep="", end="</td>")
print("</tr></table>",ctlHTMLEnd)
