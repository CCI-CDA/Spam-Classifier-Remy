FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn

COPY . .

EXPOSE 8000

CMD [ "fastapi", "run", "server.py", "--host", "0.0.0.0", "--port", "8000" ]