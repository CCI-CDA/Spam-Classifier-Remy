# Projet formation CDA 2024

## chapitre 1

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

# Serveur FastAPI

```bash
 # run server 'dev'
 fastapi dev server.py --host 0.0.0.0 --port 3000
```

```bash
 # run 'prod'
 fastapi run server.py --host 0.0.0.0 --port 3000
```
