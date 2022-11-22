myTable = [5,85,45,35,41,2,77,61]


for i in range(len(myTable)):
    for j in range(len(myTable)):
        if (myTable[i] > myTable[j]):
            stock = myTable[i]
            myTable.pop(i)
            myTable.append(stock)

print(myTable)