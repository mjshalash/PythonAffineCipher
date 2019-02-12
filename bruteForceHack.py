import sys, os, mainAffine

def main():
    myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG '<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
    bruteHackAffine(myMessage)

def bruteHackAffine(message):
    # Flag to signal if possible solution found
    foundFlag = 0

    file = open("common.txt", "r")

    # Encryption/Decryption paramaters
    commonWords = file.read()
   
    print('Hacking...')
    
    # brute-force by looping through every possible key
    for key in range(256 ** 2):
        keyA = mainAffine.getKeyParts(key)[0]
        if mainAffine.gcd(keyA, 256) != 1:      # Continue through next iteration if not relatively prime
            continue

        decryptedText = mainAffine.decrypt(key, message)
        
        for word in decryptedText.split():
            for commonWord in commonWords.split():
                if foundFlag == 0 and word == commonWord:
                        foundFlag = 1

        if foundFlag:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
            
           

    return None



if __name__ == '__main__':
    main()