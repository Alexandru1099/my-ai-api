# Folosim Python 3.10
FROM python:3.10

# Setăm directorul de lucru
WORKDIR /app

# Copiem toate fișierele în container
COPY . /app

# Instalăm pachetele necesare
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expunem portul 8000
EXPOSE 8000

# Pornim API-ul corect (dacă e în `app/`)
CMD ["uvicorn", "app.flan_t5_api:app", "--host", "0.0.0.0", "--port", "8000"]
