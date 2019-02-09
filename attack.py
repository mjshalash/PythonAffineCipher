# Malik Shalash
# Affine Cipher Attack
# 1/31/2019

# import statements
import sys, os, collections

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
    print(ord(firstComChar))
    print(ord(secondComChar))

    # Equation would be set up as so
    # y1 = (ax1 + b) % m  where y1 = asciiSpace and x1 = encryptedSpace ... etc. etc.


def getCommon(list):
    # Return just the charachter
    return list[0]
    


if __name__ == '__main__':
    main()