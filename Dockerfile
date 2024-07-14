FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Tentukan direktori kerja
WORKDIR /app

# Salin requirements.txt dan instal dependensi Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke direktori kerja
COPY . /app/

# Perintah untuk menjalankan aplikasi
CMD ["python", "main.py"]
