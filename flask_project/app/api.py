from flask import Blueprint, request, render_template
from bson import json_util
import json
import os
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
from image import Image
import random
from app.db import get_weather, get_crimes

images_api_v1 = Blueprint(
    'images_api_v1',  'images_api_v1', url_prefix='/api/v1/images')

crime_api_v1 = Blueprint(
    'crime_api_v1',  'crime_api_v1',  url_prefix='/api/v1/crime' )


@images_api_v1.route('/all', methods=['GET'])
def api_search_images():

    weather = get_weather()
    
    response = {
        "weather": weather,
    }

    page_sanitized = json.loads(json_util.dumps(response))
    return page_sanitized


@crime_api_v1.route('/all', methods=['GET'])
def api_search_crime():
    # determine the filters
    filters = {}
    return_filters = {}

    # finally use the database and get what is necessary
    (crimes, total_num_entries) = get_crimes(filters)

    response = {
        "total_results": total_num_entries,
        "filters": return_filters,
        "crimes": crimes,
    }

    page_sanitized = json.loads(json_util.dumps(response))
    return page_sanitized

@images_api_v1.route('/randomone', methods=['GET'])
def api_get_random_image():
    def pick_random_file(folder1, folder2):
        files1 = os.listdir(folder1)
        files2 = os.listdir(folder2)
        # Combine both file lists
        all_files = [(folder1, f) for f in files1] + [(folder2, f) for f in files2]
        # Pick a random file from the combined list
        chosen_folder, chosen_file = random.choice(all_files)
        chosen_file_path = os.path.join(chosen_folder, chosen_file)
        if 'NORMAL' in chosen_folder:
            image_label = 'Normal'
        else:
            image_label = 'Pneumonia'
        return chosen_file_path, image_label

    filters = {"fields": ["geometry", "properties.START_DATE", "properties.LATITUDE", "properties.LONGITUDE", "properties.OFFENSE"]}
    (crimes, total_num_entries) = get_crimes(filters)

    response = {
        "total_results": total_num_entries,
        "filters": filters,
        "crimes": crimes,
    }

    page_sanitized = json.loads(json_util.dumps(response))
    return page_sanitized

@images_api_v1.route('/predict', methods=['GET'])
def api_predict_diagnosis(image):
    def predict(image_path):
        image = Image.open(image_path).convert('RGB')
        image_resized = image.resize((224,224))
        # Convert image to array, normalize, and dimension
        image_array = np.array(image_resized)
        x = image_array / 255.0
        x = np.expand_dims(x, axis=0)
        prediction = model.predict(x)
        if prediction >= 0.5:
            print('Model Prediction: Pneumonia')
            plt.imshow(image)
        else:
            print('Model Prediction: Normal')
            plt.imshow(image)