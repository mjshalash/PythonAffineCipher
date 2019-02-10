# Malik Shalash
# Affine Cipher Attack
# 1/31/2019

# import statements
import sys, os, collections, mainAffine

# Global variables for two most common ascii values
asciiE = 69
asciiSpace = 32

# Read in encrypted file
def main():
    
    # Define file to be read in
    file = open("testFiles/test.txt", "r")
    myMessage = file.read()

    # Assume that " " and "e" are the two most common charachters in encypted text
    firstCount = collections.Counter(myMessage).most_common(2)[0]   # Assume this charachter is ' '
    secondCount = collections.Counter(myMessage).most_common(2)[1]   # Assume this charachter is e

    # Get the encypted charachters
    firstComChar = getCommon(firstCount)
    secondComChar = getCommon(secondCount)

    # Find the ascii values for encrypted charachters
    firstAscii = ord(firstComChar)
    secondAscii = ord(secondComChar)

    # Print statements for verification
    print("Most Common Charachter: %s with Ascii value: %d" % (firstComChar, firstAscii))
    print("Second Most Common Charachter: %s with Ascii value: %d" % (secondComChar, secondAscii))

    # Final Equation Variables
    y3 = 0
    x3 = 0

    # Relevant equations
    # y1 = (ax1 + b) % 256
    # b = y1 - ax1 % 256
    # a = 141 (y1 - y2)
    #
    # encryptedSpace = (a(asciiSpace) + b) % 256         First Equation
    # encryptedE = (a(asciiE) + b) % 256                 Second Equation

    #----------------- Attempt Number 1--------------------#
    # y3 = secondAscii - firstAscii
    # x3 = asciiE - asciiSpace

    # # Now one equation is y3 = a(x3)
    # inv = mainAffine.findModInverse(x3, len(mainAffine.ASCIISymbols)) # Find modular inverse of x3 and 256

    # a = (inv*y3) % len(mainAffine.ASCIISymbols) # This is what "a" equals
    # print("This is a: ", a)
    # print(" ")
    
    # x4 = x3
    # print("x4 is: ", x4)
    # x4Inv = mainAffine.findModInverse(x4, len(ASCIISymbols))
    # print("x4Inv is: ", x4Inv)

    # b = (x4Inv)*((asciiSpace*secondAscii) - (asciiE*firstAscii))
    
    
    #----------------- Attempt Number 2 --------------------#
    a = (141*(firstAscii - secondAscii)) % (len(mainAffine.ASCIISymbols))
    b = (firstAscii - (a)*(asciiSpace)) % (len(mainAffine.ASCIISymbols))

    print("This is a: ", (a % (len(mainAffine.ASCIISymbols))))
    print("This is b: ", (b % (len(mainAffine.ASCIISymbols))))

    # Apply a and b to decryption formula
    decryptViaAttack(a, b, myMessage)

#Affine Decryption function
def decryptViaAttack(a, b, message):
    keyA = a

    print("keyA is: ", keyA)
    print("Length is: ", len(mainAffine.ASCIISymbols))

    keyB = b
    mainAffine.checkKeys(keyA, keyB, 'd')

    plaintext = ''
    modInverseOfKeyA = mainAffine.findModInverse(keyA, len(mainAffine.ASCIISymbols))

    print("Mod Inverse of A is: ", modInverseOfKeyA)

    for symbol in message:
        if symbol in mainAffine.ASCIISymbols:
            # decrypt this symbol
            symIndex = mainAffine.ASCIISymbols.find(symbol)
            plaintext += mainAffine.ASCIISymbols[(symIndex - keyB) * modInverseOfKeyA % len(mainAffine.ASCIISymbols)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    print(plaintext)

def getCommon(list):
    # Return just the charachter
    return list[0]
    


if __name__ == '__main__':
    main()