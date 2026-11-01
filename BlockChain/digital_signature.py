import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes



message= b"thi is my transaction"

private_key= rsa.generate_private_key(public_exponent=65537,key_size=2048)
public_key=private_key.public_key()

signature=private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

print(signature.hex())

try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()


    )
    print("valid signature")
except InvalidSignature:
    print("signature invalid")

