#Python 2.7.12
#Run program to be prompted to enter input

def findB(a, n):
    start = round(-(n/2.0)) + 1
    end = float((n/2))
    if end < 0:
        for i in range((int(end) + 1), int(start)):
            if i % n == a % n:
                return i
    else:
        for i in range(int(start), (int(end) + 1) ):
            if i % n == a % n:
                return i
    return 0

print "This program will return to you b = a mod n"
while True:
    user_input_a = raw_input("Enter a: ")
    user_input_n = raw_input("Enter n: ")
    try:
        int(user_input_a)
        int(user_input_n)
    except ValueError:
        print "Please enter a real, positive integer"
    else:
        print "B:", findB(int(user_input_a), int(user_input_n))
        break