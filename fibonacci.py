
#Python 2.7.6
#Run program to be prompted to enter input

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

isStillRunning = True
print "This program will return to you the nth fibonacci value of a number"
while isStillRunning:
    user_input = raw_input("Enter n: ")
    try:
        int(user_input)
        if int(user_input) < 0:
            raise ValueError
    except ValueError:
        print "Please enter a real, positive integer"
    else:
        user_input = int(user_input)
        for i, n in zip(range(user_input + 1), fibonacci()):
            if i == user_input:
                print "Number you entered:", i, " nth fibonacci number", n
        isStillRunning = False
