#!/usr/bin/python3

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from otherRSAfunctions import *

# Function that prints private and public RSA keys
def printRsaKeys(privateRSA,publicRSA):

    print("####################")
    print("#   Private RSA :  #")
    print("####################\n")
    print("d : ",privateRSA[0])
    print("n : ",privateRSA[1])

    print("\n####################")
    print("#   Public RSA :   #")
    print("####################\n")
    print("e : ",publicRSA[0])
    print("n : ",publicRSA[1])
