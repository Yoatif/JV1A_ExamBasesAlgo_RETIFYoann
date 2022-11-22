joueur_1 = "X"
joueur_2 = "O"
tour = 0
case = ["","","","","","","","",""]
win = 0
complet = 0

#afficher la grille
print ("",case[0],"_|_", case[1],"_|_", case[2],"\n",case [3],"_|_", case[4],"_|_", case[5],"\n", case[6]," | ", case[7]," | ", case[8])


#boucle jeu
while win == 0 or complet == 0:
    if (tour = 9 and testhorizontal == false and testVertical == false and testDiagonal == false):
        complet = 1