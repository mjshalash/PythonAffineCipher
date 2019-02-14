import sys, os, random, string, collections

def main():
    
    # Menu
    print("""
    1.) Encrypt
    2.) Decrypt
    3.) Attack
    """)

    res = input("What would you like to do? \n")

    if res == '1':
        print("Encrypting... \n")
        useCipher('e')
    elif res == '2':
        print("Decrypting... \n")
        useCipher('d')
    elif res == '3':
        print("Attacking")
    else:
        print("Error")

def useCipher(mode):
    # Define file to be read in
    file = open("testFiles/test.txt", "r")

    # Encryption/Decryption paramaters
    myMessage = file.read()
    myKey = getRandomKey()
    myMode = mode

    # Determines whether we are encrypting a message or decrypting a message
    if myMode == 'e':
        encrypt(myKey, myMessage)
    elif myMode == 'd':
        decrypt(myKey, myMessage)

    file.close()

# Get Key Parts
def getKeyParts(key):
    a = key // 256    # Quotient 
    b = key % 256     # Remainder
    return (a, b)     # Return tuple of both keys

# Validate the key parts are strong enough to create a secure encryption
def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'e':
        sys.exit('a cannot equal one.')
    if keyB == 0 and mode == 'e':
        sys.exit('b cannot equal zero.')
    if keyA < 0 or keyB < 0 or keyB > 255:
        sys.exit('a must be greater than 0 and b must be between 0 and %s.' % (255))
    if gcd(keyA, 256) != 1:
        sys.exit('a and the set size are not relatively prime.')  

# Affine Encryption function
def encrypt(key, message):
    origA, origB = getKeyParts(key)  # Establish both key and key b by returning a tuple from the function

    checkKeys(origA, origB, 'e')     # Validate that keys are correct
    cipherText = ''
    for symbol in message:           # For each letter in the .txt file, run it through encryption function 
        symIndex = ord(symbol)
        cipherText += chr((symIndex * origA + origB) % 256)

    print("Ciphertext Recieved: "+ cipherText)
    print()
    print()
    # Run decryption
    print("Decrypted Plaintext: "+ decrypt(key, cipherText))
    
    # Run attack function to see if same keys can be achieved
    print("Running Attack....Standby!")
    attackCipher(cipherText)
    
# Affine Decryption function
def decrypt(key, message):
    # Get same key parts utilized in encryption
    keyA, keyB = getKeyParts(key)

    # Validate keys are recieved properly
    checkKeys(keyA, keyB, 'd')
    plaintext = ''
    
    # Find modular inverse of part a of the key
    modInverseOfKeyA = findModInverse(keyA, 256)

    # For each plaintext symbol in the message, run through decryption function
    for symbol in message:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - keyB) * modInverseOfKeyA % 256)
    
    return plaintext

# Generates a random key to improve probabilistic security
def getRandomKey():
    while True:
        keyA = random.randint(2, 256)
        keyB = random.randint(2, 256)
        if gcd(keyA, 256) == 1:
            return keyA * 256 + keyB

# --------------------Attack Section -------------------- 
def attackCipher(ciphertext):
    asciiSpace = 32
    
    # Final Equation Variables
    a = 0
    b = 0

    # Find the two most common charachters in the cipher text
    firstAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[0]))   # Assume this charachter is ' '
    secondAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[1]))   # Assume this charachter is e

    a = (115*(firstAscii - secondAscii)) % (256) # 115 is inverse of 101 - 32 = 69
    b = (firstAscii - (a)*(asciiSpace)) % (256)

    checkKeys(a, b, 'd')

    plaintext = ''
    modInverseOfKeyA = findModInverse(a, 256)

    for symbol in ciphertext:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - b) * modInverseOfKeyA % 256)
    
    print("Attack result: ", plaintext)

# Used to get only the charachter from the "most common charachter" collections function
def getCommon(list):
    return list[0]

# --------------------Neccessary Math Section -------------------- 
# Finding greatest common divisor
def gcd(x, y):
    while x != 0:
        x, y = y % x, x
    return y

# Euclidean Algorithm
# Returns inverse of a with mod m
def findModInverse(a, m) : 
    a = a % m    
    
    # Loop through values of x from 1 to m
    for x in range(1, m) :

        # If x times a results in a modulus remainder of 1 then we found our inverse!
        if ((a * x) % m == 1):

            # Return x as it is the inverse 
            return x 
    
    # If none is found then return 1 by default
    return 1

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main()