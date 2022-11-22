
case = ["","","","","","","","",""]
tour = 0

print ("",case[0],"_|_", case[1],"_|_", case[2],"\n",case [3],"_|_", case[4],"_|_", case[5],"\n", case[6]," | ", case[7]," | ", case[8])


caseLibre = False
while(not caseLibre):
    numeroCase= int(input("quel case veux tu jouer ?"))
    if (numeroCase <9 and case[numeroCase] !="O" and case[numeroCase] !="X"):
        caseLibre = True
symbole="O"
if (tour%2==1):
    symoble="X"
case[numeroCase] = symbole

print ("",case[0],"_|_", case[1],"_|_", case[2],"\n",case [3],"_|_", case[4],"_|_", case[5],"\n", case[6]," | ", case[7]," | ", case[8])

