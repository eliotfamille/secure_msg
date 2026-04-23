# load_keys.py
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def load_private(path: str):
    with open(path, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend())
def load_public(path: str):
    with open(path, 'rb') as f:
        return serialization.load_pem_public_key(
            f.read(), backend=default_backend())
