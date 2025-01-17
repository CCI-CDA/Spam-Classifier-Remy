#import de pandas qui permet de lire le fichier .txt SMSSpamCollection.txt'
import pandas as pd 
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import os
import sqlite3

#Initialise pandas pour qu'il puisse convertir le fichier en liste utilisable avec label et message en clé
df = pd.read_csv('data/SMSSpamCollection.txt', sep='\t', header=None, names=['label', 'message'])

app = FastAPI()

db_name = os.getenv("DB_NAME","spam_classifier.db")
con = sqlite3.connect(db_name,check_same_thread=False)




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
@app.get("/check", response_class=HTMLResponse)
def check_message(request: Request, message: str,user:str):
    result = classify_message(message)
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO users(username,password,quota) VALUES (?,?,?)",(user,None,0))
    res = cursor.execute("""
        SELECT id FROM users where username = ?
    """,[user]) 

    cursor.execute("""
        INSERT INTO predictions (user_id, message, classification)
        VALUES (?, ?, ?)
    """, (res.fetchone()[0], message, result)) 
    con.commit()   
    return templates.TemplateResponse(
        "check.html", {"request": request, "message": message, "classification": result}
    )

@app.get("/history", response_class=HTMLResponse)
def history(request: Request):
    cursor = con.cursor()
    res = cursor.execute("""
        SELECT * FROM predictions INNER JOIN users WHERE predictions.user_id=users.id
    """,) 
    return templates.TemplateResponse(
        "history.html", {"request": request,"result":res.fetchall()}
    )




    
