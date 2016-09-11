isNotFinished = True
print "This program will return to you the potential m values, given n,"
while isNotFinished:
    input = raw_input('Enter n: ')
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
        print output
        isNotFinished = False
