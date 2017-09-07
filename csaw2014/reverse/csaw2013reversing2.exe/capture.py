#Establish an array of the encrypted flag one byte hex strings
enc = [0xBB, 0xCC, 0xA0, 0xBC, 0xDC, 0xD1, 0xBE, 0xB8, 0xCD, 0xCF, 0xBE, 0xAE, 0xD2, 0xC4, 0xAB, 0x82, 0xD2, 0xD9, 0x93, 0xB3, 0xD4, 0xDE, 0x93, 0xA9, 0xD3, 0xCB, 0xB8, 0x82, 0xD3, 0xCB, 0xBE, 0xB9, 0x9A, 0xD7, 0xCC, 0xDD ]

#Establish the array of hex strings which will be xoring
key = [ 0xbb, 0xaa, 0xcc, 0xdd ]

#Establish the string which will store the decrypted flag
flag = ""

#Establish variables for iteration counting
i = 0
j = 0

#Establish the for loop which will do the xoring
for x in enc:
    flag += chr(enc[i] ^ key[j])
    i += 1
    j += 1
    #Reset the second iteration counter after four iterations
    if j > 3:
        j = 0

#Print the flag
print flag