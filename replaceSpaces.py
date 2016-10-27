#Write a method to replace all spaces in a string with %20

def replaceSpaces(myString):
    finString = ""
    for char in myString:
        if char == " ":
            finString += "%20"
        else:
            finString += char
    return finString

myString = "Hello this is my very long string for the purpose of testing!"

print replaceSpaces(myString)
