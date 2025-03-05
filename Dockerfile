# Folosim imaginea oficială de Python
FROM python:3.10

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem toate fișierele în container
COPY . /app

# Instalăm pachetele necesare
RUN pip install --no-cache-dir fastapi uvicorn transformers torch

# Expunem portul 8000
EXPOSE 8000

# Comanda de start a API-ului
CMD ["uvicorn", "flan_t5_api:app", "--host", "0.0.0.0", "--port", "8000"]
