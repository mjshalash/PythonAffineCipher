# Malik Shalash
# Affine Cipher Attack
# 1/31/2019

# import statements
import sys, os, collections

# Read in encrypted file
def main():
    
    # Define file to be read in
    file = open("testFiles/test.txt", "r")
    myMessage = file.read()

    # Assume that " " and "e" are the two most common charachters in whatever needs to be decrypted
    firstCount = collections.Counter(myMessage).most_common(2)[0]   # Assume this charachter is ' '
    secondCount = collections.Counter(myMessage).most_common(2)[1]   # Assume this charachter is e

    # Get the charachters
    firstComChar = getCommon(firstCount)
    secondComChar = getCommon(secondCount)

    # Find the ascii values for charachters
    print(ord(firstComChar))
    print(ord(secondComChar))

def getCommon(list):
    # Return just the charachter
    return list[0]
    



if __name__ == '__main__':
    main()