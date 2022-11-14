import os
import time

#get info
uid=input("Enter your UID: ")
bcc=input("Enter the BCC of the UID: ")
sak=input("Enter your SAK: ")
atqa=input("Enter your ATQA: ")
size=input("What size is the card. enter 1 or 4 only: ")

#mangle it.
suid=(' '.join(uid[i:i+2] for i in range(0, len(uid), 2)))
satqa=(' '.join(atqa[i:i+2] for i in range(0, len(atqa), 2)))

if (len(uid) == 8):
    builder=(uid + bcc + sak + atqa + "0000000000000000")
    block0=(' '.join(builder[i:i+2] for i in range(0, len(builder), 2)))
            
elif (len(uid) == 14):
    builder=(uid + bcc + sak + atqa + "0000000000")
    block0=(' '.join(builder[i:i+2] for i in range(0, len(builder), 2)))
            
else:
    print("Re Check your UID and try again")



def main():
    contents=("""Filetype: Flipper NFC device
Version: 2
# Nfc device type can be UID, Mifare Ultralight, Mifare Classic
Device type: Mifare Classic
# UID, ATQA and SAK are common for all formats
UID: """+(suid)+"""
ATQA: """+(satqa)+"""
SAK: """+(sak)+"""
# Mifare Classic specific data
Mifare Classic type: """+(size)+"""K
Data format version: 2
# Mifare Classic blocks, '??' means unknown data
Block 0: """+(block0)+"""
Block 1: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 2: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 3: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 5: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 7: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 8: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 11: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 12: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 13: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 15: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 16: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 17: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 18: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 19: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 21: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 22: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 23: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 24: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 25: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 26: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 27: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 28: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 29: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 31: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 32: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 33: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 34: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 35: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 36: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 37: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 38: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 39: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 41: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 42: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 43: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 44: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 45: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 46: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 47: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 48: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 49: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 51: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 52: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 53: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 54: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 55: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 56: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 57: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 58: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 59: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF
Block 60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 61: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 62: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Block 63: FF FF FF FF FF FF FF 07 80 69 FF FF FF FF FF FF""")

    file = open(uid+".nfc","w")
    file.write(contents)
    file.close()

    file = open(uid+".nfc","r")
    print(file.read())
main()


    
