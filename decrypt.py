#fo=open("pqr.png","rb")
fo = open(input (str("Please enter the name of the file you wish to decrypt:" )),"rb")

files=fo.read()

fo.close()

image=bytearray(files)
#key=48
key= int(input("Enter key"))

for index , value in enumerate(image):
    image[index]=value^key

#fo=open("lmn.png","wb")
fo = open(input (str("Please enter the name of the file you wish to save the decrypted file with:" )),"wb")

fo.write(image)

fo.close()
