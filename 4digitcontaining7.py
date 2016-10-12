#How many 4 digit numbers contain a 7?
def fourDigitNumsContainSeven ():
    count = 0
    for x in range(1000, 9999):
        if "7" in str(x):
            count += 1
    return count

print fourDigitNumsContainSeven()
