def testHorizontale (case):
    for i in range (0,9,3):
        if ((case[i] == case[i+1] == case[i+2]) and (case[i]=="O" or case[i]=="X")):
            return True
    return False
def testVertical(case):
    for i in range(0, 9, 3):
        if ((case[i] == case[i+3] == case[i+6]) and (case[i]=="O" or case[i]=="X")):
            return True
    return False
def testDiagonale(case):
    if (case[4]=="O" or case[4]=="X"):
        if (case[0] == case[4] == case[8]):
            return True
        if (case[2] == case[4] == case[6]):
            return True
    return False

