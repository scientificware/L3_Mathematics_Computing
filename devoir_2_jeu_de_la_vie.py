# Jeu de la vie

import random
import copy

class Jeu_De_La_Vie :
    """Evolution d'une population de cellules suivant certaines règles"""

    # Grille contenant les cellules
    grille = []

    # Marqueur cellule
    CV = '\u2b1b' #'X'
    CM = '\u2b1c' #' '

    # Méthode construisant une grille vide de n×m :
    # C'est à dire composée uniquement de cellules mortes.
    # où m est le nombre de colonnes et n le nombre de lignes
    def __init__(self,m,n):
         liste_cellules_mortes = [[self.CM for i in range(m)] for j in range(n)]
         self.grille = liste_cellules_mortes

    # Méthode renvoyant une chaîne de caractères représentant la grille.
    def __str__(self):
        représentation = ''
        for j in range(len(self.grille)) :
            for i in range(len(self.grille[j])) :
                représentation = représentation +str(self.grille[j][i])
            représentation = représentation + '\n'
        return représentation

    # Méthode mettant à jour la grille en passant à la génération suivante.
    def évolution(self):

        generation_suivante = copy.deepcopy(self.grille)
        imax = len(self.grille[1])-1
        jmax = len(self.grille)-1
        
        for n in range(0,jmax+1) :
            for m in range(0,imax+1) :
                nb = self.nb_cell_vivantes(m,n)
                est_vivante = (self.grille[n][m]==self.CV)
                if est_vivante :
                    if not(nb==2 or nb==3) :
                        generation_suivante[n][m]=self.CM
                else :
                    if nb==3 :
                        generation_suivante[n][m]=self.CV
        self.grille = copy.deepcopy(generation_suivante)

    # Méthode renvoyant le nombre de cellules vivantes autour d'une cellule donnée
    def nb_cell_vivantes(self,i,j) :
        imax = min(i+1,len(self.grille[1])-1)
        jmax = min(j+1,len(self.grille)-1)
        imin = max(i-1,0)
        jmin = max(j-1,0)
        nbCelViv = 0
        for n in range(jmin,jmax+1):
            for m in range(imin,imax+1):
                if( not(m==i and n==j) and self.grille[n][m]==self.CV) :
                    nbCelViv += 1
        return nbCelViv

    # Méthode ressuscitant k cellule(s) morte(s) choisie(s) aléatoirement.
    def aléas(self,k) :
        liste_cellules_mortes = []
        imax = len(self.grille[0])-1           
        jmax = len(self.grille)-1

        # Etablir la liste des cellules mortes.
        for n in range(0,jmax+1):
            for m in range(0,imax+1):
                if self.grille[n][m] == self.CM :
                    liste_cellules_mortes.append([m,n])

        # Resurrection des cellules sélectionnées
        nbCelMor = len(liste_cellules_mortes)
        if k>=nbCelMor :
            # Ressusciter toutes les cellules mortes.
            self.grille = [[self.CV for i in range(imax+1)] for j in range(jmax+1)]
        else :
            liste_cellules_mortes = random.sample(liste_cellules_mortes,k)
            for i in range(0, len(liste_cellules_mortes)):
                # Ressusciter cette cellule.
                self.grille[liste_cellules_mortes[i][1]][liste_cellules_mortes[i][0]] = self.CV

    # Méthode ressuscitant une cellule désignée par ses coordonnées.
    # Coordonnées : i numéro de colonne, j numéro de ligne.
    def créer(self,i,j) :
        imax = len(self.grille[0])           
        jmax = len(self.grille)
        try :
            if 0<=i<imax and 0<=j<jmax :
                self.grille[j][i] = self.CV
                return True
            else :
                raise ValueError('Cellule hors grille')
        except ValueError as message :
            print('(',i,',',j,')',' Cellule hors grille')
            return False
        

    # Méthode fagocytant une cellule désignée par ses coordonnées.
    # Coordonnées : i numéro de colonne, j numéro de ligne.
    def fag(self,i,j) :
        imax = len(self.grille[0])           
        jmax = len(self.grille)
        try :
            if 0<=i<imax and 0<=j<jmax :
                self.grille[j][i] = self.CM
                return True
            else :
                raise ValueError('Cellule hors grille')
        except ValueError as message :
            print('(',i,',',j,')',' Cellule hors grille')
            return False
 
# Test de base   
class Test_base_Jeu_De_La_Vie :
    
    def __init__(self):
        Jeu = Jeu_De_La_Vie(12,8)
        print('Test grille initiale de 12 colonnes et 8 lignes\n',Jeu,sep='',end='')
        
        Jeu.créer(5,4)
        Jeu.créer(5,3)
        Jeu.créer(6,1)
        Jeu.créer(6,3)
        Jeu.créer(1,3)
        print('Test création de 5 cellules\n', Jeu, sep='',end='')

        print('Test cellule hors grille\n',Jeu,sep='',end='')
        Jeu.créer(50,10)

        print("Test nombre cellule(s) vivante(s) au voisinage d'une cellule donnée\n",Jeu,sep='',end='')
        print('(00,03) cernée par ',Jeu.nb_cell_vivantes(0,3),' cellule(s) vivante(s)')
        print('(00,04) cernée par ',Jeu.nb_cell_vivantes(0,4),' cellule(s) vivante(s)')
        print('(00,05) cernée par ',Jeu.nb_cell_vivantes(0,5),' cellule(s) vivante(s)')
        print('(00,06) cernée par ',Jeu.nb_cell_vivantes(0,6),' cellule(s) vivante(s)')
        print('(00,07) cernée par ',Jeu.nb_cell_vivantes(0,7),' cellule(s) vivante(s)')

        print('(02,02) cernée par ',Jeu.nb_cell_vivantes(2,2),' cellule(s) vivante(s)')
        print('(03,02) cernée par ',Jeu.nb_cell_vivantes(3,2),' cellule(s) vivante(s)')
        print('(04,02) cernée par ',Jeu.nb_cell_vivantes(4,2),' cellule(s) vivante(s)')
        print('(05,02) cernée par ',Jeu.nb_cell_vivantes(5,2),' cellule(s) vivante(s)')
        print('(06,02) cernée par ',Jeu.nb_cell_vivantes(6,2),' cellule(s) vivante(s)')

        print('(07,02) cernée par ',Jeu.nb_cell_vivantes(7,2),' cellule(s) vivante(s)')
        print('(08,02) cernée par ',Jeu.nb_cell_vivantes(8,2),' cellule(s) vivante(s)')
        print('(09,02) cernée par ',Jeu.nb_cell_vivantes(9,2),' cellule(s) vivante(s)')
        print('(10,02) cernée par ',Jeu.nb_cell_vivantes(10,2),' cellule(s) vivante(s)')
        print('(11,02) cernée par ',Jeu.nb_cell_vivantes(11,2),' cellule(s) vivante(s)')

        Jeu.évolution()
        print('Test grille après 1 seule évolution\n',Jeu,sep='',end='')

        Jeu.évolution()
        print('Test grille après 2 évolutions\n',Jeu,sep='',end='')

        Jeu.évolution()
        print('Test grille après 3 évolutions\n',Jeu,sep='',end='')

        Jeu.aléas(10)
        print('Test grille après 10 résurrections aléatoires demandées\n',Jeu,sep='',end='')

        Jeu.aléas(2000)
        print('Test grille après 2 000 résurrections demandées\n',Jeu,sep='',end='')

# Tests automatiques et utilisateur
choix=0
JeuTest = Jeu_De_La_Vie(1,1)
while not(choix==3):
    choix=0
    while not(1<=choix<=3):
        try :
            choix = int(input(
                '\nMenu des tests disponibles\n'+
                '1-Test de base.\n'+
                '2-Test utilisateur.\n'+
                '3-Fin de test.\n'+
                'Choix : '))
        except ValueError as message :
            print ('\nSeuls choix possibles 1,2 ou 3.\n')
    if choix == 1 :
        Test_base_Jeu_De_La_Vie()
    elif choix == 2 :
        choix2=0
        while not(choix2==6):
            choix2=0
            while not(1<=choix2<=6):
                print('\nGrille actuelle\n',JeuTest,sep='',end='')
                try :
                    choix2 = int( input(
                        "Menu actions utilisateurs\n"+
                        "1-Nouvelle grille.\n"+
                        "2-Création manuelle de cellules vivantes.\n"+
                        "3-Suppression manuelle de cellules vivantes.\n"+
                        "4-Création automatique de cellules vivantes.\n"+
                        "5-Lancer l'évolution.\n"+
                        "6-Retour menu précédent.\n"+
                        "Choix :"))
                except ValueError as message :
                    print ('\nSeuls choix possibles 1,2,3,4,5 ou 6.\n')
                    
            # Création d'une nouvelle grille.
            if choix2==1 :
                nbColonne = 0
                nbLigne = 0
                print('\nGrille actuelle\n',JeuTest,sep='',end='')
                while nbLigne<1 or nbColonne<1 :
                    print ('Seuls les entiers non nuls sont acceptés.')
                    try :
                        nbColonne = int(input('Nombre de colonne de la grille : '))
                        nbLigne = int(input('Nombre de ligne de la grille : '))
                    except ValueError as message :
                        pass
                JeuTest = Jeu_De_La_Vie(nbColonne,nbLigne)
                print('\nNouvelle grille de ',nbColonne,' colonne(s) et ',
                      nbLigne,' ligne(s)\n',JeuTest,sep='',end='')

            # Création manuelle de cellules vivantes.
            elif choix2==2 :
                nbCellule = 0
                autreCellule = True
                print('\nGrille actuelle\n',JeuTest,sep='',end='')
                while autreCellule :
                    print ('Seuls les entiers sont acceptés.\n'+
                           'Entrer "fin" pour terminer la création de cellules')
                    try :
                        numColonne = int(input('Numéro de colonne de la cellule à créer : '))
                        numLigne = int(input('Numéro de ligne de la cellule à créer : '))
                        if JeuTest.créer(numColonne,numLigne) :
                            nbCellule += 1
                            print('\nNouvelle grille avec ',nbCellule,
                                  ' cellule(s) crée(s)\n',JeuTest,sep='',end='')
                    except ValueError as message :
                        if str(message)=="invalid literal for int() with base 10: 'fin'" :
                            autreCellule = False

            # Suppression manuelle de cellules vivantes.
            elif choix2==3 :
                nbCellule = 0
                autreCellule = True
                print('\nGrille actuelle\n',JeuTest,sep='',end='')
                while autreCellule :
                    print ('Seuls les entiers sont acceptés.\n'+
                           'Entrer "fin" pour terminer la suppression de cellules')
                    try :
                        numColonne = int(input('Numéro de colonne de la cellule à supprimer : '))
                        numLigne = int(input('Numéro de ligne de la cellule à supprimer : '))
                        if JeuTest.fag(numColonne,numLigne) :
                            nbCellule += 1
                            print('\nNouvelle grille avec ',nbCellule,
                                  ' cellule(s) supprimée(s)\n',JeuTest,sep='',end='')
                    except ValueError as message :
                        if str(message)=="invalid literal for int() with base 10: 'fin'" :
                            autreCellule = False
                
            elif choix2==4 :
                nbCellule = -1
                while nbCellule<0 :
                    print('\nGrille actuelle\n',JeuTest,sep='',end='')
                    print ('Seuls les entiers sont acceptés.')
                    try :
                        nbCellule = int(input('Entrer le nombre de cellules à ressusciter :'))
                    except ValueError as message :
                        pass
                if nbCellule>0 :
                    JeuTest.aléas(nbCellule)
                print('\nNouvelle grille avec ',nbCellule,
                      ' cellule(s) ressuscitée(s)\n',JeuTest,sep='',end='')
                
            elif choix2==5 :
                nbEvolution = -1
                print('\nGrille actuelle\n',JeuTest,sep='',end='')
                while nbEvolution<0 :
                    print ('Seuls les entiers sont acceptés.')
                    try :
                        nbEvolution = int(input("Entrer le nombre d'évolutions : "))
                    except ValueError as message :
                        pass
                if nbEvolution>0 :
                    for i in range(1,nbEvolution+1):
                        JeuTest.évolution()
                        print('\nNouvelle grille après ',i,' évolution(s)\n',JeuTest,sep='',end='')
                
            else :
                pass
    else:
        pass
