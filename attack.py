# Malik Shalash
# Affine Cipher Attack
# 1/31/2019

# import statements
import sys, os, collections, mainAffine

# Read in encrypted file
def attackCipher(ciphertext):
    asciiSpace = 32
    asciiE = 101
    
    # Final Equation Variables
    x3 = 0
    y3 = 0
    a = 0
    b = 0

    # Assume that " " and "e" are the two most common charachters in encypted text
    firstAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[0]))   # Assume this charachter is ' '
    secondAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[1]))   # Assume this charachter is e

    a = (115*(firstAscii - secondAscii)) % (256) # 115 is inverse of 101 - 32 = 69
    b = (firstAscii - (a)*(asciiSpace)) % (256)

    print("This is a: ", (a % 256))
    print("This is b: ", (b % 256))

    mainAffine.checkKeys(a, b, 'd')

    plaintext = ''
    modInverseOfKeyA = mainAffine.findModInverse(a, 256)

    print("Mod Inverse of A is: ", modInverseOfKeyA)

    for symbol in ciphertext:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - b) * modInverseOfKeyA % 256)
    
    print(plaintext)

# Get only the charachter from the list
def getCommon(list):
    
    return list[0]
