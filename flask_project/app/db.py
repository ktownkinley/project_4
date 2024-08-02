"""
This module contains all database interfacing methods for the MFlix
application. You will be working on this file for the majority of M220P.

Each method has a short description, and the methods you must implement have
docstrings with a short explanation of the task.

Look out for TODO markers for additional help. Good luck!
"""

from app.mongo_cred import uri
from flask import current_app, g, Flask
from flask_pymongo import PyMongo


# Use LocalProxy to read the global db instance with just `db`
app = Flask(__name__)
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
db = mongo.db

def get_crime():
    """
    Finds and returns movies by country.
    Returns a list of dictionaries, each dictionary contains a title and an _id.
    """
    try:

        """
        Ticket: Projection

        Write a query that matches movies with the countries in the "countries"
        list, but only returns the title and _id of each movie.

        Remember that in MongoDB, the $in operator can be used with a list to
        match one or more values of a specific field.
        """

        return list(db.crimes.find())

    except Exception as e:
        return e


def build_query_sort_project(filters):
    """
    Builds the `query` predicate, `sort` and `projection` attributes for a given
    filters dictionary.
    """
    query = {}
    fields = {}

    project = None

    #         """
    #         Ticket: Text and Subfield Search

    #         Given a genre in the "filters" object, construct a query that
    #         searches MongoDB for movies with that genre.
    #         """

    #         # TODO: Text and Subfield Search
    #         # Construct a query that will search for the chosen genre.
    #         query = {}
    if filters:
        if "fields" in filters:
            fields["_id"] = 0
            for x in filters["fields"]:
                fields[x] = 1
            

    return query, fields, project


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
