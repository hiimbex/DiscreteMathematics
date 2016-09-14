isNotFinished = True
print "This program will return to you the potential n values, given m,"
while isNotFinished:
    input = raw_input('Enter m: ')
    try:
        int(input)
    except ValueError:
        print "That was not an acceptable integer."
    else:
        input = int(input)
        output = []
        output.append(input)
        if (0 - input != input):
            output.append(0 - input)
        otherValuesFound = True
        negative = False
        if input <= 0:
            negative = True
            x = input - 1
        else:
            x = input + 1
        while otherValuesFound:
            if float(input)/x > 0.5 or float(input)/x == 0.5:
                output.append(x)
                output.append(-x)
                if negative:
                    x = x - 1
                else:
                    x = x + 1
            else:
                otherValuesFound = False
        print output
        isNotFinished = False
