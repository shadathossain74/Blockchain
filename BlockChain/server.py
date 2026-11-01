
import socket
import json
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Connected with:", addr)

data = b""
while True:
    chunk = conn.recv(4096)
    if not chunk:
        break
    data += chunk

received = json.loads(data.decode())

message = received["message"].encode()
signature = base64.b64decode(received["signature"])
public_key = serialization.load_pem_public_key(
    received["public_key"].encode()
)

print("Received Message:", message.decode())

try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Valid Signature")
except InvalidSignature:
    print("Invalid Signature")

conn.close()
server.close()
