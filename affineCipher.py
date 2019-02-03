# Malik Shalash
# Affine Cipher
# 1/31/2019

import sys, cryptomath, random

# What is allowed to be decrypted
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

# Main Function
def main():
    myMessage = "IPv[f5 =$-Rvnf={svs-j-RV-v$fvB-v[){{-sv1N$-{{1^-N$v1Fv1$v[f={svs-[-1V-v)vw=5)Nv1N$fvB-{1-V1N^v$w)$v1$vn)jvw=5)NUIv<P{)NvK=R1N^"
    myKey = 2487
    myMode = 'd'

    # Print statements for logging purposes
    print('Key: %s' % (myKey))
    print('Size of Symbols: %d' %(len(SYMBOLS)))

    # Determines whether we are encrypting a message or decrypting a message
    if myMode == 'e':
        answer = encrypt(myKey, myMessage)
    elif myMode == 'd':
        answer = decrypt(myKey, myMessage)
    

    # Print statements for logging purposes
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
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

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()