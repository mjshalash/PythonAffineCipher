import sys, os, random, string
import attack, cryptomath

# Contains all the possible ascii charachters that can be printed on the screen
ASCIISymbols = string.printable

def main():
    useCipher()


def exec_menu(choice):
    if choice == 1:
        # Run Encryption/Decryption Program
        # TODO: Need to add option for decryption or encryption
        useCipher()
        print(choice)
    elif choice == 2:
        # Run Hacking Program
        print(choice)
    else:
        # Default Message    
        print(choice)


def useCipher():
    # For testing ascii values
    for i in range(1, 255):
        ch = chr(i)
        print(i, "=", ch)

    # Define file to be read in
    file = open("testFiles/test.txt", "r")

    myMessage = file.read()
    myKey = 8981
    myMode = 'd'

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
    if cryptomath.gcd(keyA, len(ASCIISymbols)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(ASCIISymbols)))  

# Affine Encryption function
def encrypt(key, message):
    a, b = getKeyParts(key)  # Establish both key and key b by returning a tuple from the function

    print('Key A is %d', a)
    print('Key B is %d', b)

    checkKeys(a, b, 'e')     # Validate that keys are correct
    cipherText = ''
    for symbol in message:
            if symbol in ASCIISymbols:
                # Encrypt Specific Symbol
                symIndex = ASCIISymbols.find(symbol)
                cipherText += ASCIISymbols[(symIndex * a + b) % len(ASCIISymbols)]
            else:
                # Append the symbol to our current solution
                cipherText += symbol
    return cipherText

#Affine Decryption function
def decrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(ASCIISymbols))

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
        if cryptomath.gcd(keyA, len(ASCIISymbols)) == 1:
            return keyA * len(ASCIISymbols) + keyB

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main()