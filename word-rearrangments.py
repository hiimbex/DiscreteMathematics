
# Python 2.7.6
#Run program to be prompted for input, (autocapitalizes all input)

from itertools import permutations
isRunning = True
print "This program will return to you all permutations of a word"
while isRunning:
    n = raw_input("Enter a word: ").upper()
    try:
        str(n)
    except ValueError:
        print "Please enter a real word"
    else:
        permutations = [''.join(p) for p in permutations(n)]
        # print "All Permutations: ", permutations
        permutationsSet = set(permutations)
        #Getting unique values
        print "Unique Permutations: ", list(permutationsSet)
        print "Total Unique Permutations: ", len(permutationsSet)
        isRunning = False
