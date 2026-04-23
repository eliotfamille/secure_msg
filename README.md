Pour installer ton projet sur une machine propre, voici la procédure complète, étape par étape, depuis zéro.
1. Installer Python
·	Sur Linux/base debian:
·	sudo apt update
·	sudo apt install python3 python3-pip python3-venv

2. Préparer le dossier de travail
Place les fichiers de code (les 7 fichiers .py) dans un dossier dédié :
Bash
mkdir mon_projet_crypto cd mon_projet_crypto

3. Créer un environnement isolé
Cela permet d'installer les outils sans polluer ton système :

python3 -m venv venv
source venv/bin/activate 

4. Installer la bibliothèque nécessaire
Toujours avec l'environnement activé, installez le moteur de cryptographie :

pip install cryptography

5. Vérification finale
Tu peux maintenant lancer la démonstration :

# 1. Générer les clés python3 
main.py --action keygen 
# 2. Envoyer un message
 python3 main.py --action send --msg "Bonjour Eliot" > msg.json 
# 3. Lire le message python3 
main.py --action receive --packet msg.json 
