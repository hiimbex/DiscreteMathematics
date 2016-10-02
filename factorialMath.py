import math
print "Enter an n"
n = int(raw_input())
print "Enter an r"
r = int(raw_input())
def permutation(n, r):
    return math.factorial(n)/(math.factorial(n-r))
print permutation(n, r)
