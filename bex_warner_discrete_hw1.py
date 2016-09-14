isNotFinished = True
print "This program will return to you the potential n values, given m,"
while isNotFinished:
    input = raw_input('Enter m: ')
    #checks if input was an integer
    try:
        int(input)
    except ValueError:
        print "That was not an acceptable integer."
    # re-asks for input in the int wasn't a real int and restarts at top of while loop
    else:
        input = int(input)
        output = []
        output.append(input)
        #adds input to output list and inverse of input
        if (-input != input):
            output.append(-input)
        otherValuesFound = True
        negative = False
        # checks if number is negative so that x will be scaled in the right direction
        if input <= 0:
            negative = True
            n = input - 1
        else:
            n = input + 1
        while otherValuesFound:
            if float(input)/n > 0.5 or float(input)/n == 0.5:
                output.append(n)
                output.append(-n)
                if negative:
                    n = n - 1
                else:
                    n = n + 1
                # adds x to output while it's less than or equal to .05
            else:
                otherValuesFound = False
                # exits while loop when x no longer meets the conditions
        print output
        isNotFinished = False
        # prints output and quits main program while loop
