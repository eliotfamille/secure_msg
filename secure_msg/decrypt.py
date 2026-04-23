# decrypt.py
import base64, json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from verify import verify_signature

def decrypt_message(packet: dict, private_key, sender_pub_key) -> str:
    # ① Reconstruire le contenu signé
    raw = json.dumps(
    {k: packet[k] for k in ["enc_aes_key","nonce","ciphertext"]}
    ).encode()
    
    # ② Vérifier la signature AVANT tout déchiffrement
    if not verify_signature(raw, packet['signature'], sender_pub_key):
        raise ValueError('Signature invalide — message rejeté.')

    # ③ Déchiffrer la clé AES
    aes_key = private_key.decrypt(
        #dechiffre le binaire
        base64.b64decode(packet['enc_aes_key']),
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(), label=None))
    
    # ④ Déchiffrer le message
    aesgcm = AESGCM(aes_key)
    nonce = base64.b64decode(packet['nonce'])
    ciphertext = base64.b64decode(packet['ciphertext'])
    
    return aesgcm.decrypt(nonce, ciphertext, None).decode()
