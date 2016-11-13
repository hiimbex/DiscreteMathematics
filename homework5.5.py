#Python 2.7.12
#Run program to be prompted to enter input

def gcd(m,n):
    m,n=abs(m),abs(n)
    m,n=max(m,n),min(m,n)
    mm,nn=m,n #Keep original values
    M=[1,0]
    N=[0,1]
    while n != 0:
        q,r=m//n,m%n
        M[0],N[0]=N[0],M[0]-N[0]*q
        M[1],N[1]=N[1],M[1]-N[1]*q
        m,n=n,r
    print("{:d}*{:d}+{:d}*{:d}={:d}".format(M[0],mm,M[1],nn,m))
    return M[1], m

print "This program will return to you a ^ k mod n"
while True:
    userInputA = input("Input a number m: ")
    userInputB = input("Input a the modulo (n): ")
    try:
        int(userInputA)
        int(userInputB)
    except ValueError:
        print "Please enter a real, positive integer"
    else:
        inverse, m = gcd(userInputA, userInputB)
        if m == 1:
            print inverse
        else:
            print "No inverse found for given m"
        break
