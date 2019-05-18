# Codage Huffman

class Arborescence_Huffman :
    """Elément d'une arborescence"""

    def __init__(self,c,n,ar1,ar2):
        '''Initialisateur'''
        self.__caractere = c
        self.__poids = n
        self.__filsG = ar1
        self.__filsD = ar2
        self.majTableCo()
        self.__ident=''

    def __str__(self):
        '''Méthode renvoyant une chaîne de caractères représentant la sous-arborescence'''
        ch = ''
        schD = ''
        schG = ''
        if self.__caractere == '' :
            schD  = "┬1" + str(self.__filsD)
            if self.__filsD.donneCar() =='' :
                n = schD.count("\n")
                schD = schD.replace("\n","\n│ ",n-1)
            schG = "└0" + str(self.__filsG)
            if self.__filsG.donneCar() =='' :
                n = schG.count("\n")
                schG = schG.replace("\n","\n  ",n-1)                  
            ch = schD + schG        
        else :
            ch= '╢'+self.__caractere+'\n'  
        return ch


    def donneEti(self):
        '''Méthode renvoyant l'étiquette (la valeur entière associée à la racine)'''
        return self.__poids


    def donneCar(self):
        '''Méthode renvoyant le caractère associé, le cas échéant, à la racine'''
        return self.__caractere
    
    
    def donneFilsG(self):
        '''Méthode renvoyant la sous-arborescence gauche si elle existe'''
        return self.__filsG

    
    def donneFilsD(self):
        '''Méthode renvoyant la sous-arborescence droite si elle existe'''
        return self.__filsD


    def fusionne(self, arb):
        '''Méthode fusionnant l'arborescence courante avec une autre'''
        # Renvoie une nouvelle arborescence ayant pour fils gauche l'arborescence courant
        # et pour fils droit la seconde arborescence.
        nArbo = Arborescence_Huffman("",self.__poids + arb.donneEti(),self,arb)
        return nArbo


    def majTableCo(self) :
        '''Mise à jour de la table de correspondance'''
        self.__tableCo = {}
        if self.__caractere!='' and self.donneFilsG()==None and self.donneFilsD()==None :
            self.__tableCo = {self.__caractere:''}
        else :
            self.__tCo = self.donneFilsG().donneTableCo()

            for car,bits in self.__tCo.items() :
                self.__tableCo[car]='0' + bits
                
            self.__tCo = self.donneFilsD().donneTableCo()

            for car,bits in self.__tCo.items() :
                self.__tableCo[car]='1' + bits


    def donneTableCo(self) :
        '''Méthode renvoyant la table de correspondance entre chaque caractère de'''
        return self.__tableCo


class Codage_Huffman :
    
    def __init__(self, chaineRef) :
        '''Initialisateur qui construit l'arborescence'''
        self.__codee = ''
        self.__arbre = []
        for c in chaineRef :
            occ = chaineRef.count(c)
            if not(c in self.__codee) :
                self.__arbre.append(Arborescence_Huffman(c,occ,None,None))
                self.__codee += c

        while len(self.__arbre) > 1 :
            self.__arD = self.__arbre.pop(1)
            self.__arbre[0]= self.__arbre[0].fusionne(self.__arD)
            self.__arbre = sorted(self.__arbre , key = lambda Arborescence_Huffman : Arborescence_Huffman.donneEti())  
        

    def coder(self, ch) :
        '''Méthode qui prend en entrée une chaîne et qui renvoie une suite de bits'''
        self.__phrase = ch
        self.__tabCod = self.donneArbre().donneTableCo()
        for c in self.__phrase :
            self.__phrase = self.__phrase.replace(c,self.__tabCod[c])
        return self.__phrase
    
   
    def décoder(self, bit) :
        '''Méthode qui prend en entrée une suite de bits et qui renvoie une chaîne'''
        phrase = ''
        racine = self.donneArbre()
        branche = racine
        for b in bit :
            if b =='0':
                branche = branche.donneFilsG()
            else :
                branche = branche.donneFilsD()    
            if branche.donneCar()!='' :
                phrase = phrase + branche.donneCar()
                branche = racine
   
        return phrase

    def donneArbre(self) :
        return self.__arbre[0]
 

# Interface utilisateur
choix=0
phrsR = "un exemple d'arborescence de huffman"
cdH = Codage_Huffman(phrsR)
while not(choix==6):
    choix=0
    while not(1<=choix<=6):
        try :
            choix = int(input(
                "\nCodage selon l\'algorithme d\'Huffman"
                "\nMenu principal\n"+
                "1-Test de base.\n"+
                "2-Afficher le dictionnaire et l'arborescence.\n"+
                "3-Modifier la phrase de référence.\n"+
                "4-Coder une phrase.\n"+
                "5-Décoder une suite de bits.\n"+
                "6-Terminer l'application.\n"+
                "Choix : "))
        except ValueError as message :
            print ('\nSeuls choix possibles 1,2 ... ou 6.\n')
            
        if choix == 1 :
            phraseRef = "un exemple d'arborescence de huffman"
            code_Huffman = Codage_Huffman(phraseRef)
            phrase = "aux"
            print('\nCodage Huffman de la phrase "',phrase,'" en utilisant la chaine de référence "',phraseRef,'"')
            print('Dictionnaire de codage construit à partir de la chaine de référence')
            print(code_Huffman.donneArbre().donneTableCo())
            print('Phrase codée -> ', code_Huffman.coder(phrase))

            
            suiteBit = '1010110001110'
            print('\nDécodage Huffman de la suite de bit "',suiteBit,'" en utilisant la chaine de référence "',phraseRef,'"')
            print('\nArborescence construite à partir de la chaine de référence')
            print(code_Huffman.donneArbre())
            print('Suite de bits décodée -> ', code_Huffman.décoder(suiteBit))
            
        elif choix == 2 :
            print('\nDictionnaire de codage et arborescence construits à partir de la chaine de référence "',phrsR,'"')
            print(cdH.donneArbre().donneTableCo())
            print(cdH.donneArbre())

            
        # Saisie d'une chaîne de caractères de référence,
        # Construction d'une instance du codage de Huffman sur la base de cette chaîne de référence,
        elif choix == 3 :
            valide = False
            cAut =" abcdefghijklmnopqrstuvwxyz?!';,.-+/*0123456789"
            while not valide :
                mem = phrsR
                phrsR = str(input("\nEntrer une chaine de caractère de référence (minuscules sans accent, ponctuation, espace uniquement) : "))
                valide = True
                for c in phrsR :
                    if cAut.count(c)<1 :
                        valide = False
                if valide :
                    if len(phrsR)>0 :
                        cdH = Codage_Huffman(phrsR)
                    else :
                        phrsR = mem
                        print("Votre saisie est vide. La phrase de référence ne sera pas modifiée ! ")

        # Saisie des chaînes de caractères, représentation selon le codage de Huffman et affichage,
        elif choix == 4 :
            valide = False
            while not valide :
                listC = cdH.donneArbre().donneTableCo()
                print('\n',sorted(listC))
                phrase = str(input("\nEntrer une phrase (utiliser uniquement les caractères ci-dessus) : "))
                valide = True
                for c in phrase :
                    if phrsR.count(c)<1:
                        valide = False
                if valide :
                    if len(phrase)>0 :
                        code = cdH.coder(phrase)
                        print('Phrase codée sur ', len(code) ,' bit(s) -> ', code)
                    else :
                        print("Vous n'avez entré aucune phrase ! ")
                        
        # Saisie des suites de bits et affichage des chaînes de caractères correspondantes.
        elif choix == 5 :
            valide = False
            cAut ='01'
            while not valide :
                # Saisie des suites de bits et affichage des chaînes de caractères correspondantes.
                suiteBits = str(input("\nEntrer votre suite binaire (utiliser uniquement des 0 et des 1) : "))
                valide = True
                for c in suiteBits :
                    if cAut.count(c)<1 :
                        valide = False
                if valide :
                    if len(suiteBits)>0 :
                        print('Suite de bit décodée -> ', cdH.décoder(suiteBits))
                    else :
                        print("Vous n'avez entré aucune suite binaire ! ")
