# Program for finding number of involuntary or trivial keys in affine cipher

import sys, os, array

def main():
    # Array of integers to hold values of a that satisfy first condition of involuntary
    candidateA = array.array('i')
    
    candidateB = array.array('i')
    
    invKeyCount = 0
    

    # Find a's that satisfy a^2 being equal to 1 mod 256
    for a in range(0, 256):
        if ((a**2) % 256) == 1:
            candidateA.append(a)

    
    for a in candidateA:
        for b in range(0, 256):
            if (b*(1+a) % 256) == 0:
                candidateB.append(b)


    print("Involuntary Values for a found for Z256:")
    for a in candidateA:
        print(a)
    
    print("Involuntary Values for b found for Z256:")
    for b in candidateB:
        if(b == 0):
            print("-------------")
        print(b)
        invKeyCount = invKeyCount + 1

    print('Total number of involuntary keys is: %d' %invKeyCount)
    print("")

    # Finding involuntary keys will require using a and b pair to solve if
    # x = (ax + b) % 256 is true aka the key does not do anything
    for x in range(1, 256):
        for a in range(0, 256):
            for b in range (0, 256):
                if (x*a + b) == x:
                   print('%d %d %d' % (x, a, b)) 

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main()