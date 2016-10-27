def gcd(a,b):
    """
        Find the greatest common divisor
    """
    if not isinstance(a,int) or not isinstance(b,int):
        return None

    a,b=abs(a),abs(b)
    a,b=max(a,b),min(a,b)

    while b!=0:
        a,b=b,a%b

    return a

def main():
    userInputA = input("Input a number (then hit enter): ")
    userInputB = input("Input a second number (then hit enter): ")
    return gcd(userInputA, userInputB)

print main()