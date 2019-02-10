import sys, os, mainAffine

def main():
    myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG '<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
    bruteHackAffine(myMessage)

def bruteHackAffine(message):
    print('Hacking...')
    
    # brute-force by looping through every possible key
    for key in range(len(mainAffine.ASCIISymbols) ** 2):
        keyA = mainAffine.getKeyParts(key)[0]
        if mainAffine.gcd(keyA, len(mainAffine.ASCIISymbols)) != 1:
            continue

        decryptedText = mainAffine.decrypt(key, message)
        print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

    return None



if __name__ == '__main__':
    main()