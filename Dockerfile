FROM python:3.11.9-bookworm

WORKDIR /app

COPY requirements.txt ./
COPY service_account.json ./
COPY ./.chainlit ./
COPY chainlit.md ./
COPY app.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["chainlit", "run", "-h", "--port", "8080", "app.py"]