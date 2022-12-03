def afficheGrille (tableau):
    for i in range (0,9,3):
        print (tableau[i], tableau[i+1], tableau[i+2],)

def ajoutesymoble (tableau,numéroDeTour):
    caseValable = False
    while(not caseValable):
        numeroCase= int(input("quel case ?"))
        if (numeroCase <9 and tableau[numeroCase] !="O" and tableau[numeroCase] !="X"):
            caseValable = True
    symbole="O"
    if (numéroDeTour%2==1):
        symoble="X"
    tableau[numeroCase] = symbole
def testVictoireHorizontale (tableau):
    for i in range (0,9,3):
        if ((tableau[i] == tableau[i+1] == tableau[i+2]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False
def testVictoireVerticale(tableau):
    for i in range(0, 9, 3):
        if ((tableau[i] == tableau[i+3] == tableau[i+6]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False
def testVictoireDiagonale(tableau):
    if (tableau[4]=="O" or tableau[4]=="X"):
        if (tableau[0] == tableau[4] == tableau[8]):
            return True
        if (tableau[0] == tableau[4] == tableau[8]):
            return True
    return False

#ici débute le programme
grille = (" "," "," "," "," "," "," "," "," ")
tour = 1
victoire = False
while (not victoire and tour < 9):
    tour +=1
    afficheGrille(grille)
    ajoutesymoble(grille,tour)
    victoire = testVictoireHorizontale(grille) or testVictoireVerticale(grille) or testVictoireDiagonale(grille)
if (victoire):
    print ("GG")
else:
    print("noob")