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

    # Final Equation Variables
    y3 = 0
    x3 = 0

    # Equation would be set up as so
    # y1 = (ax1 + b) % m  Encryption Function
    # encryptedSpace = (a(asciiSpace) + b) % 256         First Equation
    # encryptedE = (a(asciiE) + b) % 256                 Second Equation

    y3 = secondAscii - firstAscii
    x3 = asciiE - asciiSpace

    # Now one equation is y3 = a(x3)
    inv = mainAffine.findModInverse(x3, len(mainAffine.ASCIISymbols)) # Find modular inverse of x3 and 256

    a = (inv*y3) % 256 # This is what "a" equals
    print("This is a: ", a)
    print(" ")
    
    x4 = x3
    print("x4 is: ", x4)
    x4Inv = mainAffine.findModInverse(x4, len(mainAffine.ASCIISymbols))
    print("x4Inv is: ", x4Inv)

    b = (x4Inv)*((asciiSpace*secondAscii) - (asciiE*firstAscii))
    
    
    print("This is b: ", b)

    # Apply a and b to decryption formula
    mainAffine

def getCommon(list):
    # Return just the charachter
    return list[0]
    


if __name__ == '__main__':
    main()