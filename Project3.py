########################################################################################################################## 
# Project3.py
# Step 1 - Elliptic Curve Diffie-Hellman exchange to establish a shared secret.  Use a NIST approved curve. (Module 5)
# Step 2 - For each chunk of public information sent generate an RSA Digital Signature. (Module 6)
# Step 3 - Validate the RSA digital signature of the packets you receive. (Module 6)
# Step 4 - Once you have a shared key encrypt a message using AES in GCM mode (not in our notes but not too different). (Module 3)
# Written by - Ravi Padma
##########################################################################################################################
import os
from Crypto.PublicKey import ECC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import binascii

print("Start of Project 3.................\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
secretKey = ECC.generate(curve='P-256')
f = open('myprivatekey.pem','wt')
f.write(secretKey.export_key(format='PEM'))
f.close()
f = open('myprivatekey.pem','rt')
secretKey = ECC.import_key(f.read())
print("Step 1 - Elliptic Curve Diffie-Hellman exchange to establish a shared secret.  Use a NIST approved curve. .................\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
print (secretKey)
print("-------------------------------------------------------------------------------------------------------------------------------------\n")

print("Step 2 - For each chunk of public information sent generate an RSA Digital Signature. .................\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
# Generate a new RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Generate a message to be signed
message = b"Hello, Bob! This class is awesome - Alice"

# Generate the signature using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Signature:", binascii.hexlify(signature))
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
# Validate the signature using the public key
print("Step 3 - Validate the RSA digital signature of the packets you receive .................\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid for ", message)
except:
    print("Signature is invalid ", message)

# Validate the signature using the public key
message = b"Hello, Bob! This class is awesome - Bob"
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid for ", message)
except:
    print("Signature is invalid ", message)
print("-------------------------------------------------------------------------------------------------------------------------------------\n")

print("Step 4 - Once you have a shared key encrypt a message using AES in GCM mode  .................\n")
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
# Generate Alice's private key and public key
alice_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
alice_public_key = alice_private_key.public_key()

# Generate Bob's private key and public key
bob_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
bob_public_key = bob_private_key.public_key()

# Perform ECDH to generate a shared key
shared_key = alice_private_key.exchange(ec.ECDH(), bob_public_key)
shared_key1 = bob_private_key.exchange(ec.ECDH(), alice_public_key)
print("Shared Key:\n", shared_key)
#print("Shared Key:\n", shared_key1)
print("-------------------------------------------------------------------------------------------------------------------------------------\n")

# Create an instance of AESGCM using the shared key
aesgcm = AESGCM(shared_key)
aesgcm1 = AESGCM(shared_key)

# Nonce to be used for encryption
nonce = b"12345678"

# Encrypt the Alice's message using AES-GCM
message = b"Hello, Bob! This class is awesome - Alice"
ciphertext = aesgcm.encrypt(
    nonce,
    message,
    associated_data=None
)

# Print the ciphertext
print("Alice sending encrypted message to Bob.................\n")
print("Ciphertext received by Bob:\n", ciphertext)

# Decrypt the ciphertext using AES-GCM
plaintext = aesgcm.decrypt(
    nonce,
    ciphertext,
    associated_data=None
)

# Print the decrypted plaintext
print("Plaintext converted by Bob:\n", plaintext)

# Encrypt the Bob's response using AES-GCM
message = b"Hello, Alice! You bet - Bob"
ciphertext = aesgcm1.encrypt(
    nonce,
    message,
    associated_data=None
)

# Print the ciphertext
print("-------------------------------------------------------------------------------------------------------------------------------------\n")
print("Bob responding with encrypted message to Alice.................\n")
print("Ciphertext  received by Alice:\n", ciphertext)

# Decrypt the ciphertext using AES-GCM
plaintext = aesgcm1.decrypt(
    nonce,
    ciphertext,
    associated_data=None
)

# Print the decrypted plaintext
print("Plaintext converted by Alice:\n", plaintext)