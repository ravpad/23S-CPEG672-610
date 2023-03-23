##########################################################################################################################
# AES_Image.py
# Image Encryption and Decryption with different AES Modes
# Modes - ECB(Electronic Code Book), CBC(Cipher Block Chaining), CFB(Cipher FeedBack), OFB(Output FeedBack), CTR (Counter)
# Written by - Ravi Padma
##########################################################################################################################

import sys, os 
from base64 import b64encode
import binascii
import cv2
import numpy as np
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from PIL import Image 
import PIL

# Set mode
def int_of_string(s):
    return int(binascii.hexlify(s), 16)

# Set sizes
keySize = 16

# Start Encryption ----------------------------------------------------------------------------------------------
# Load original image
imagefile = input("Enter the Path for image with filename with extention: ")
print(imagefile)
#imagefile="tree.jpg"
imageOrig = cv2.imread(imagefile)

mod = input ("Enter mode :\n 1 = AES.MODE_ECB \n 2 = AES.MODE_CBC \n 3 = AES.MODE_CFB  \n 4 = AES.MODE_OFB \n 5 = AES.MODE_CTR \n Option:")

#Set configuration for different modes
if(mod == '1'):
    mode = AES.MODE_ECB 
    ivSize = 0

if(mod == '2'):
    mode = AES.MODE_CBC
    ivSize = AES.block_size

if(mod == '3'):
    mode = AES.MODE_CFB
    ivSize = AES.block_size

if(mod == '4'):
    mode = AES.MODE_OFB
    ivSize = AES.block_size

if(mod == '5'):
    mode = AES.MODE_CTR
    ivSize = AES.block_size

#print(mod,mode)
#print(str(mod) + " mode is selected. Please check popup image")

rowOrig, columnOrig, depthOrig = imageOrig.shape
# Check for minimum width
minWidth = (AES.block_size + AES.block_size) // depthOrig + 1
if columnOrig < minWidth:
    print('The minimum width of the image must be {} pixels, so that IV and padding can be stored in a single additional row!'.format(minWidth))
    sys.exit()

# Display original image
cv2.imshow("Original image", imageOrig)
cv2.waitKey()

# Convert original image data to bytes
imageOrigBytes = imageOrig.tobytes()

# Encrypt
key = b'I Love the Class'
iv = b'InitiatizionVect'
print("Key Length: ", len(key) , " and IV Length: " , len(iv))
print("Key: ", key , " Hex Value of Key: ", key.hex(), " and IV: " , iv , "Hex Value of IV: ", iv.hex())

if(mod == '1'):
    print("ECB Encrypt")
    #key = get_random_bytes(keySize)
    iv = get_random_bytes(ivSize)
    cipher = AES.new(key, AES.MODE_ECB)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)

    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)

if(mod == '2'):
    print("CBC Encrypt")
    #key = get_random_bytes(keySize)
    #iv = get_random_bytes(ivSize)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)
    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)

if(mod == '3'):
    print("CFB Encrypt")
    #key = get_random_bytes(keySize)
    #iv = get_random_bytes(ivSize)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)

    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)
    
if(mod == '4'):
    print("OFB Encrypt")
    #key = get_random_bytes(keySize)
    #iv = get_random_bytes(ivSize)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)

    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)

if(mod == '5'):
    print("CTR Encrypt")
    #key = get_random_bytes(keySize)
    iv = get_random_bytes(ivSize)
    ctr = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)
    print(ctr)
    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - ivSize - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)

# Display encrypted image
cv2.imshow("Encrypted image", imageEncrypted)
cv2.imwrite(os.path.splitext(imagefile)[0] +"_encrypt" + os.path.splitext(imagefile)[1], imageEncrypted)
cv2.waitKey()

# Decrypt
if(mod == '1'):
    print("ECB Decrypt")
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    iv = encryptedBytes[:ivSize]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]
    cipher = AES.new(key, AES.MODE_ECB)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

if(mod == '2'):
    print("CBC Decrypt")
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    iv = encryptedBytes[:ivSize]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

if(mod == '3'):
    print("CFB Decrypt")
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    #iv = encryptedBytes[:ivSize]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]

    cipher = AES.new(key, AES.MODE_CFB,iv=iv)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

if(mod == '4'):
    print("OFB Decrypt")
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    #iv = encryptedBytes[:ivSize]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]

    cipher = AES.new(key, AES.MODE_OFB,iv=iv)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

if(mod == '5'):
    print("CTR Decrypt")
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    #iv = encryptedBytes[:ivSize]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]

    cipher = AES.new(key, AES.MODE_CTR,  counter=ctr)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

# Display decrypted image
cv2.imshow("Decrypted Image", decryptedImage)
cv2.imwrite(os.path.splitext(imagefile)[0] +"_decrypt" + os.path.splitext(imagefile)[1], decryptedImage)
cv2.waitKey()

# Close all windows
cv2.destroyAllWindows()