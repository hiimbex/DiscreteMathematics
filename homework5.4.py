import math

def findB(a, n):
    start = round(-(n/2.0)) + 1
    end = float((n/2))
    #print start, end
    for i in range(int(start), (int(end) + 1) ):
        if i % n == a % n:
            print i

findB(11,2)