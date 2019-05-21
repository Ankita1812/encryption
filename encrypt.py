fo = open(input (str("Please enter the name of the file you wish to encrypt:" )),"rb")

files=fo.read()

fo.close()

image=bytearray(files)

#key=48
key= int(input("Enter key"))

for index , value in enumerate(image):
    image[index]=value^key

fo = open(input (str("Please enter the name of the file you wish to save the encrypted file with:" )),"wb")

fo.write(image)

fo.close()
