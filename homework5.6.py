#Python 2.7.12
#Run program to be prompted to enter input

def modraise(a,k,n):
    ans = 1
    for i in range(k):
        ans *= a
        ans %= n
    return ans

print "This program will return to you a ^ k mod n"
while True:
    userInputA = input("Input a number a: ")
    userInputK = input("Input a second number k: ")
    userInputN = input("Input a third number n: ")
    try:
        int(userInputA)
        int(userInputK)
        int(userInputN)
        if int(userInputN) == 0:
            raise ValueError
    except ValueError:
        print "Please enter a real, positive integer"
    else:
        print modraise(userInputA, userInputK, userInputN)
        break