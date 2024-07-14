import json
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
import requests

# Membuat Web App Sederhana Menggunakan Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Prediksi Sentimen"

# Membuat API Endpoint dalam Web App sebagai Model Serving
MODEL_PATH = "sentiment-detection-model/1"
model = tf.keras.models.load_model(MODEL_PATH)

def data_preprocessing(text):
    processed_text = text.lower()
    return {"instances": [processed_text]}

@app.route("/predict", methods=["POST"])
def predict():
    request_json = request.json
    text = request_json.get("text")
    data = data_preprocessing(text)

    # Kirim data ke TensorFlow Serving
    response = requests.post(MODEL_PATH, json=data)
    prediction = response.json()

    # Ambil prediksi
    sentiment_score = prediction['predictions'][0][0]
    sentiment_label = "positif" if sentiment_score > 0.5 else "negatif"

    return jsonify({"sentiment": sentiment_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
