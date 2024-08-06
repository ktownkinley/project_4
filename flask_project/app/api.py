from flask import Blueprint, request, render_template, jsonify
from bson import json_util
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from app.db import retrieve_image, get_random_image
import base64

images_api_v1 = Blueprint(
    'images_api_v1',  'images_api_v1', url_prefix='/api/v1/images')

model = load_model('chest_Xray.keras')

@images_api_v1.route('/randomone', methods=['GET'])
def api_get_random_image():
    image_data, choice, image_id = get_random_image()

    # base64 encode the image to send back to JS
    base64_data = base64.b64encode(image_data.getvalue()).decode('utf-8')
    mime_type = "image/jpeg"
    choice = choice.split('.')[0]

    return jsonify({"image_data": base64_data, "mime_type": mime_type, "choice": choice, "image_id": image_id})

@images_api_v1.route('/predict/<image_id>/<choice>', methods=['GET'])
def api_predict_diagnosis(image_id, choice):
    image, final_choice = retrieve_image(image_id, choice)
    image = Image.open(image).convert('RGB')
    image_resized = image.resize((224,224))
    # Convert image to array, normalize, and dimension
    image_array = np.array(image_resized)
    x = image_array / 255.0
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x)
    if prediction >= 0.5:
        model_choice = 'pneumonia'
    else:
        model_choice = 'normal'
    return jsonify({'model': model_choice})
