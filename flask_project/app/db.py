from bson import ObjectId
from app.mongo_cred import uri
from flask import Flask
from flask_pymongo import PyMongo
import random
from io import BytesIO
import gridfs

# Use LocalProxy to read the global db instance with just `db`
app = Flask(__name__)
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
db = mongo.db

def get_random_image():
    try:
        collections = ['normal', 'pneumonia']
        choice = random.choice(collections)
        fs = gridfs.GridFS(db, choice)
        files = list(fs.find())
        if not files:
            raise ValueError("No files found in the database.")
        
        # Randomly select a file
        random_file = random.choice(files)

        # Retrieve the selected image
        grid_out = fs.get(random_file._id)
        image_data = BytesIO(grid_out.read())
        return image_data, choice, random_file._id
    except Exception as e:
        raise e


def retrieve_image(image_id, choice):
    try:
        image_id = ObjectId(image_id)
        fs = gridfs.GridFS(db, choice)
        files = list(fs.find())
        if not files:
            print("No files found in the database.")
        # Retrieve the selected image
        grid_out = fs.get(image_id)
        image_data = BytesIO(grid_out.read())
        return image_data
    except Exception as e:
        return e
