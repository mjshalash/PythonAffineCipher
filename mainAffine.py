import sys, os, random, string, collections

def main():
    print("""
    1.) Encrypt test.txt
    2.) Decrypt test.txt
    3.) Attack Encrypted test.txt
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
    myKey = 37293 #getRandomKey
    myMode = mode

    # Determines whether we are encrypting a message or decrypting a message
    # TODO Need to write back to same file with encrypted or decrypted text for easy conversion between the two
    if myMode == 'e':
        encrypt(myKey, myMessage)
    elif myMode == 'd':
        decrypt(myKey, myMessage)

    file.close()

    # Write back to test file
    # file2 = open("testFiles/test.txt", "w")
    # file2.write(answer)

# Get Key Parts
def getKeyParts(key):
    a = key // 256    # Quotient 
    b = key % 256     # Remainder
    return (a, b)     # Return tuple of both keys

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'e':
        sys.exit('a equals one.  Choose a different key.')
    if keyB == 0 and mode == 'e':
        sys.exit('b equals one.  Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > 255:
        sys.exit('a must be greater than 0 and b must be between 0 and %s.' % (255))
    if gcd(keyA, 256) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, 256))  

# Affine Encryption function
def encrypt(key, message):
    origA, origB = getKeyParts(key)  # Establish both key and key b by returning a tuple from the function

    checkKeys(origA, origB, 'e')     # Validate that keys are correct
    cipherText = ''
    for symbol in message:   # For each letter in the .txt file, run it through encryption function 
        symIndex = ord(symbol)
        cipherText += chr((symIndex * origA + origB) % 256)

    print("Ciphertext: "+ cipherText)
    print("Plaintext: "+ decrypt(key, cipherText))
    
    # Run attack function to see if same keys can be achieved
    attackCipher(cipherText, origA, origB)
    
# Affine Decryption function
def decrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'd')
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, 256)

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
def attackCipher(ciphertext, origA, origB):
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

    # Verify the attack keys are same as original encryption keys
    # If so, then attack succeeded
    if a == origA and b == origB: 
        print ("a = "+a+" = Original a: "+origA)
        print ("b = "+b+" = Original b: "+origB)
        print("Encryption Keys Found, Attack Succeeded!")
    else:
        print("Attack Failed!")

    plaintext = ''
    modInverseOfKeyA = findModInverse(a, 256)

    for symbol in ciphertext:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - b) * modInverseOfKeyA % 256)
    
    print("Attack result: ", plaintext)

# Same as attackCipher but assumes most common charachters are "a" and " "
def attackCipherASpace(ciphertext, origA, origB):
    asciiSpace = 32
    # asciiA = 97
    
    # Final Equation Variables
    a = 0
    b = 0

    # Assume that " " and "e" are the two most common charachters in encypted text
    firstAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[0]))   # Assume this charachter is ' '
    secondAscii = ord(getCommon(collections.Counter(ciphertext).most_common(2)[1]))   # Assume this charachter is a

    a = (193*(firstAscii - secondAscii)) % (256) # 193 is inverse of 97 - 32 = 65
    b = (firstAscii - (a)*(asciiSpace)) % (256)

    checkKeys(a, b, 'd')

    # Verify the attack keys are same as original encryption keys
    # If so, then attack succeeded
    if a == origA and b == origB: 
        print("Keys Match, Attack Succeeded!")
    else:
        print("Attack Failed!")

    plaintext = ''
    modInverseOfKeyA = findModInverse(a, 256)

    for symbol in ciphertext:
        symIndex = ord(symbol)
        plaintext += chr((symIndex - b) * modInverseOfKeyA % 256)
    
    print("Attack result: ", plaintext)    

# Get only the charachter from the list
def getCommon(list):
    return list[0]

# --------------------Neccessary Math Section -------------------- 
# Necessary Math operations
# Finding greatest common divisor
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

# Euclidean Algorithm
# # Returns inverse of a with mod m
def findModInverse(a, m):
    

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    
    # "Vector" One
    wI = 1 
    wJ = 0
    wK = a
    
    # "Vector" Two
    vI = 0 
    vJ = 1
    vK = m
    
    # Apply Euclidean Algorithm
    while vK != 0:
        q = wK // vK # Integer Division
        vI = (wI - q * vI)
        vJ = (wJ - q * vJ)
        vK = (wK - q * vK)
        wI = vI 
        wJ = vJ
        wK = vK
    
    return wI % m

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main()