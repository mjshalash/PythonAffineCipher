import sys, os, random, string
import attack

# Contains all the possible ascii charachters that can be printed on the screen
ASCIISymbols = string.printable

def main():
    print("""
    1.) Encrypt test.txt
    2.) Decrypt test.txt
    3.) Attack Encrypted test.txt
    """)

    res = input("What would you like to do?")

    if res == '1':
        useCipher('e')
    elif res == '2':
        useCipher('d')
    elif res == '3':
        print("Attacking")
    else:
        print("Error")

def useCipher(mode):
    # For testing ascii values
    for i in range(1, 255):
        ch = chr(i)
        print(i, "=", ch)

    # Define file to be read in
    file = open("testFiles/test.txt", "r")

    # Encryption/Decryption paramaters
    myMessage = file.read()
    myKey = getRandomKey()
    myMode = mode

    # Print statements for logging purposes
    print('Key: %s' % (myKey))
    print('Size of Symbols: %d', len(ASCIISymbols))

    # Determines whether we are encrypting a message or decrypting a message
    # TODO Need to write back to same file with encrypted or decrypted text for easy conversion between the two
    if myMode == 'e':
        answer = encrypt(myKey, myMessage)
    elif myMode == 'd':
        answer = decrypt(myKey, myMessage)
    

    # Print statements for logging purposes
    print('Key: %s' % (myKey))
    print('Result: %s' % (myMode.title()))
    print(answer)

    file.close()

    # Write back to test file
    file2 = open("testFiles/test.txt", "w")
    file2.write(answer)

# Get Key Parts
def getKeyParts(key):
    a = key // len(ASCIISymbols)    # Quotient 
    b = key % len(ASCIISymbols)     # Remainder
    return (a, b)              # Return tuple of both keys

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(ASCIISymbols) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(ASCIISymbols) - 1))
    if gcd(keyA, len(ASCIISymbols)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(ASCIISymbols)))  

# Affine Encryption function
def encrypt(key, message):
    a, b = getKeyParts(key)  # Establish both key and key b by returning a tuple from the function

    print('Key A is %d', a)
    print('Key B is %d', b)

    checkKeys(a, b, 'e')     # Validate that keys are correct
    cipherText = ''
    for symbol in message:   # For each letter in the .txt file, run it through encryption function
            #If the symbol is not some special charachter
            if symbol in ASCIISymbols:
                # Encrypt Specific Symbol
                symIndex = ASCIISymbols.find(symbol)
                cipherText += ASCIISymbols[(symIndex * a + b) % len(ASCIISymbols)]
            else:
                # Otherwise just add it to the text
                cipherText += symbol
    return cipherText

#Affine Decryption function
def decrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, len(ASCIISymbols))

    for symbol in message:
        if symbol in ASCIISymbols:
            # decrypt this symbol
            symIndex = ASCIISymbols.find(symbol)
            plaintext += ASCIISymbols[(symIndex - keyB) * modInverseOfKeyA % len(ASCIISymbols)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext

# Automatically determines a key to use in encryption of data
# TODO Need to determine a way to store the key and thus it can be automatically used for decryption
def getRandomKey():
    while True:
        keyA = random.randint(2, len(ASCIISymbols))
        keyB = random.randint(2, len(ASCIISymbols))
        if gcd(keyA, len(ASCIISymbols)) == 1:
            return keyA * len(ASCIISymbols) + keyB


# Necessary Math operations
# Finding greatest common divisor
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

# Euclidean Algorithm
def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main()