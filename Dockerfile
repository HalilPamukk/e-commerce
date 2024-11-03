# Python 3.12 imajını kullan
FROM python:3.12-slim

# Çalışma dizinini oluştur ve ayarla
RUN apt update && apt install -y nano htop && \
    mkdir -p /app/project/current/

# Sürüm bilgisini yazdır 
RUN python --version
RUN pip install --upgrade pip

# Gereksinim dosyalarını kopyala ve bağımlılıkları yükle
COPY ./requirements.txt /app/project/current/requirements.txt  
RUN pip install -r /app/project/current/requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/project/current/

# Çalışma dizinini ayarla
WORKDIR /app/project/current/
