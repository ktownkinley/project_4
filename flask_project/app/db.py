
from app.mongo_cred import uri
from flask import current_app, g, Flask
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
        collections = ['normal.files', 'pneumonia.files']
        choice = random.choice(collections)
        fs = gridfs.GridFS(db, choice)
        files = list(fs.find())
        if not files:
            print("No files found in the database.")
        # Randomly select a file
        random_file = random.choice(files)

        # Retrieve the selected image
        grid_out = fs.get(random_file._id)
        image_data = BytesIO(grid_out.read())
        return image_data, choice
    except Exception as e:
        return e


def retrieve_image(image_id, choice):
    try:
        fs = gridfs.GridFS(db, f'{choice}.files')
        files = list(fs.find())
        if not files:
            print("No files found in the database.")
        # Retrieve the selected image
        grid_out = fs.get(image_id)
        image_data = BytesIO(grid_out.read())
        return image_data, choice
    except Exception as e:
        return e


def get_crimes(filters#, page, movies_per_page
               ):
    """
    Returns a cursor to a list of movie documents.

    Based on the page number and the number of movies per page, the result may
    be skipped and limited.

    The `filters` from the API are passed to the `build_query_sort_project`
    method, which constructs a query, sort, and projection, and then that query
    is executed by this method (`get_movies`).

    Returns 2 elements in a tuple: (movies, total_num_movies)
    """
    query, fields, project = build_query_sort_project(filters)
    if fields:
        cursor = db.crimes.find(query, fields)
    else:
        cursor = db.crimes.find(query)

    total_num_crimes = 0
    total_num_crimes = db.crimes.count_documents(query)

    crimes = cursor

    return (list(crimes), total_num_crimes)


def get_weather(#filters, page, weather_per_page
                ):
    """
    Returns a cursor to a list of movie documents.

    Based on the page number and the number of movies per page, the result may
    be skipped and limited.

    The `filters` from the API are passed to the `build_query_sort_project`
    method, which constructs a query, sort, and projection, and then that query
    is executed by this method (`get_movies`).

    Returns 2 elements in a tuple: (movies, total_num_movies)
    """

    cursor = mongo.db.weather.find()

    weather = cursor

    return (list(weather))
