# Malik Shalash
# Affine Cipher
# 1/31/2019

import sys, cryptomath, random

# What is allowed to be decrypted
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

# Main Function
def main():

    # For testing ascii values
    for i in range(1, 255):
        ch = chr(i)
        print(i, "=", ch)

    # Define file to be read in
    file = open("testFiles/test.txt", "r")

    # Initial Parameters
    myMessage = file.read()
    myKey = getRandomKey()
    myMode = 'e'

    # Print statements for logging purposes
    print('Key: %s' % (myKey))
    print('Size of Symbols: %d' %(len(SYMBOLS)))

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

# Get Key Parts
def getKeyParts(key):
    a = key // len(SYMBOLS)    # Quotient 
    b = key % len(SYMBOLS)     # Remainder
    return (a, b)              # Return tuple of both keys

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))  

# Affine Encryption function
def encrypt(key, message):
    a, b = getKeyParts(key)  # Establish both key and key b by returning a tuple from the function

    print('Key A is %d', a)
    print('Key B is %d', b)

    checkKeys(a, b, 'e')     # Validate that keys are correct
    cipherText = ''
    for symbol in message:
            if symbol in SYMBOLS:
                # Encrypt Specific Symbol
                symIndex = SYMBOLS.find(symbol)
                cipherText += SYMBOLS[(symIndex * a + b) % len(SYMBOLS)]
            else:
                # Append the symbol to our current solution
                cipherText += symbol
    return cipherText

#Affine Decryption function
def decrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext

# Automatically determines a key to use in encryption of data
# TODO Need to determine a way to store the key and thus it can be automatically used for decryption
def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()