import sys, os, random, string, collections, statistics
import numpy
from scipy.stats import entropy
plainCodes = []
cipherCodes = []

def main():
    # Import ascii values from plaintext and analyze
    analyzePlaintext()

def analyzePlaintext():
    # Define file to be read in
    file = open("testFiles/test.txt", "r")

    # Encryption/Decryption paramaters
    plainSymbols = file.read()

    for char in plainSymbols:
        plainCodes.append(ord(char))
    
    print("-----------Plaintext Stats-----------")
    # Mode
    plainMode = statistics.mode(plainCodes)
    print("Mode: %d, Char: %s" %(plainMode, chr(plainMode)))

    # Mean
    plainMean = statistics.mean(plainCodes)
    print("Mean: %d, Char: %s" %(plainMean, chr(int(plainMean))))

    # Standard Deviation
    plainSTD = statistics.stdev(plainCodes)
    print("Stdev: %d," %plainSTD)
    
    # Median
    plainMedian = statistics.median(plainCodes)
    print("Median: %d, Char: %s" %(plainMedian, chr(int(plainMedian))))

    # Entropy
    messageStats = collections.Counter(plainSymbols)
    sortStats = sorted(messageStats)
    ent = findEntropy(sortStats, 256)
    print("Entropy: %f" %ent)

def analyzeCiphertext(ciphertext):
    
    for char in ciphertext:
        cipherCodes.append(ord(char))
    
    print("-----------Ciphertext Stats-----------")
    # Mode
    cipherMode = statistics.mode(cipherCodes)
    print("Mode: %d, Char: %s" %(cipherMode, chr(cipherMode)))

    # Mean
    cipherMean = statistics.mean(cipherCodes)
    print("Mean: %d, Char: %s" %(cipherMean, chr(int(cipherMean))))

    # Standard Deviation
    cipherSTD = statistics.stdev(cipherCodes)
    print("Stdev: %d," %cipherSTD)

    # Median
    cipherMedian = statistics.median(cipherCodes)
    print("Median: %d, Char: %s" %(cipherMedian, chr(int(cipherMedian))))

    # Entropy
    messageStats = collections.Counter(ciphertext)
    sortStats = sorted(messageStats)
    ent = findEntropy(sortStats, 256)
    print("Entropy: %f" %ent)

def findEntropy(labels, base=None):
    value,counts = numpy.unique(labels, return_counts=True)
    return entropy(counts, base=base)


if __name__ == "__main__":
    main()

