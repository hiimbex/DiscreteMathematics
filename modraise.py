def modraise(a,b,n):
    # a^b mod n
    # a is the number you want ot encrypt or decrypt
    # b is the encrypting or decrypting key
    # n is the modulo you use which is p*q (both prime numbers)
    ans = 1
    for i in range(b):
        ans *= a
        ans %= n
    return ans

userInputA = input("Input a number (then hit enter): ")
userInputB = input("Input a second number (then hit enter): ")
userInputC = input("Input a third number (then hit enter): ")
print modraise(userInputA, userInputB, userInputC)