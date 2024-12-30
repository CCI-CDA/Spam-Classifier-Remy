import pandas as pd 
from fastapi import FastAPI

df = pd.read_csv('data/SMSSpamCollection.txt', sep='\t', header=None, names=['label', 'message'])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

app = FastAPI()

def classify_message(message):
    spam_keywords = ['free', 'win', 'cash', 'prize', 'call now', 'urgent']
    for word in spam_keywords:
        if word in message.lower():
            return "spam"
    return "ham"

@app.get("/check")
def check_message(message: str):
    result = classify_message(message)
    return {"message": message, "classification": result}
