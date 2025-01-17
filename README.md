# Projet formation CDA 2024

## Spam Classifier mini projet

## Environnement python

```bash
 # Création de l'environnement python propre au projet
 python3.9 -m venv venv
```

```bash
 # Activation de l'environnement
 .\venv\Scripts\Activate.ps1
```

```bash
 # Import de toutes les librairies définies dans requirements
 pip install -r requirements.txt
```

```bash
#Création de la BDD
python spamdb.py
```

```bash
#Lancer un serveur de dev (ici sur le port 6400) en local
fastapi dev main.py --host 0.0.0.0 --port 6400 
#Sur la VM (en cours)
docker build -t spam-classifier-remy .
docker run -p 5700:6400 spam-classifier-remy
```


```bash
#verification si les tests fonctionnes 
pytest tests.py
```
