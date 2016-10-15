myList = [1,2,3,4,6,7,8,9,10,11,20,39,40,50,80,81,92]

def printMissNumbers(list, minNumber, maxNumber):
    for i in range(minNumber, maxNumber + 1):
        if i not in myList:
            print i

printMissNumbers(myList, 0, 100)

#Time Complexity O(N), here N is 100
