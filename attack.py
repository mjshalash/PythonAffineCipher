# Malik Shalash
# Affine Cipher Attack
# 1/31/2019

# import statements
import sys, os, collections, mainAffine

# Global variables for two most common ascii values
asciiE = 101
asciiSpace = 32

# Read in encrypted file
def attackCipher(ciphertext):
    
    # Define file to be read in
    # file = open("testFiles/test.txt", "r")
    myMessage = ciphertext

    # Assume that " " and "e" are the two most common charachters in encypted text
    firstCount = collections.Counter(myMessage).most_common(2)[0]   # Assume this charachter is ' '
    secondCount = collections.Counter(myMessage).most_common(2)[1]   # Assume this charachter is e

    # Get the encypted charachters
    firstComChar = getCommon(firstCount)
    secondComChar = getCommon(secondCount)

    # Find the ascii values for encrypted charachters
    firstAscii = ord(firstComChar)   # Space
    secondAscii = ord(secondComChar) # E

    # Print statements for verification
    print("Most Common Charachter: %s with Ascii value: %d" % (firstComChar, firstAscii))
    print("Second Most Common Charachter: %s with Ascii value: %d" % (secondComChar, secondAscii))

    # Final Equation Variables
    y3 = 0
    x3 = 0

    a = (115*(firstAscii - secondAscii)) % (256) # 115 is inverse of 101 - 32 = 69
    b = (firstAscii - (a)*(asciiSpace)) % (256)

    print("This is a: ", (a % 256))
    print("This is b: ", (b % 256))

    # Apply a and b to decryption formula
    decryptViaAttack(a, b, ciphertext)

#Affine Decryption function
def decryptViaAttack(a, b, message):
    keyA = a

    print("keyA is: ", keyA)
    print("Length is: ", 256)

    keyB = b
    mainAffine.checkKeys(keyA, keyB, 'd')

    plaintext = ''
    modInverseOfKeyA = mainAffine.findModInverse(keyA, 256)

    print("Mod Inverse of A is: ", modInverseOfKeyA)

    for symbol in message:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - keyB) * modInverseOfKeyA % 256)
    
    print(plaintext)

def getCommon(list):
    # Return just the charachter
    return list[0]
