#import de pandas qui permet de lire le fichier .txt SMSSpamCollection.txt'
import pandas as pd 
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

#Initialise pandas pour qu'il puisse convertir le fichier en liste utilisable avec label et message en clé
df = pd.read_csv('data/SMSSpamCollection.txt', sep='\t', header=None, names=['label', 'message'])



app = FastAPI()




#Fonction qui permet de détecté les spam j'ai mis une liste de mot assez bateau
def classify_message(message):
    spam_keywords = ['free', 'win', 'cash', 'prize', 'call now', 'urgent']
    for word in spam_keywords:
        if word in message.lower():
            return "spam"
    return "ham"


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

#Permet de tester les messages
@app.get("/check")
def check_message(message: str):
    result = classify_message(message)
    return {"message": message, "classification": result}
