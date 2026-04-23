# main.py
import argparse, json
from keygen import generate_rsa_keys
from encrypt import encrypt_message
from decrypt import decrypt_message
from sign import sign_message
from load_keys import load_private, load_public

p = argparse.ArgumentParser()
p.add_argument('--action', choices=['keygen','send','receive'], required=True)
p.add_argument('--msg', help='Message à envoyer')
p.add_argument('--packet', help='Fichier JSON reçu')
args = p.parse_args()
if args.action == 'keygen':
    generate_rsa_keys()
elif args.action == 'send':
    priv = load_private('private.pem')
    pub = load_public('public.pem')
    pkt = encrypt_message(args.msg, pub)
    raw = json.dumps(
        {k: pkt[k] for k in ["enc_aes_key","nonce","ciphertext"]}
    ).encode()
    pkt['signature'] = sign_message(raw, priv)
    print(json.dumps(pkt, indent=2))
elif args.action == 'receive':
    priv = load_private('private.pem')
    pub = load_public('public.pem')
    with open(args.packet) as f: pkt = json.load(f)
    print('Message reçu :', decrypt_message(pkt, priv, pub))
