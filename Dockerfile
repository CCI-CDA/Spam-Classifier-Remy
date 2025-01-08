FROM python:3.13

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn
RUN pip install fastapi[standard]
COPY . .

EXPOSE 8000

CMD [ "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000" ]