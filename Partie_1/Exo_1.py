

myTable = [5,85,45,35,41,2,77,61]

stock = myTable[0]

if (myTable[5] < stock):
    stock2 = myTable[5]
    myTable[5] = stock
    myTable[0] = stock2

print(myTable)