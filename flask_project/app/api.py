from flask import Blueprint, request
from bson import json_util
import json
from app.db import get_weather, get_crimes

weather_api_v1 = Blueprint(
    'weather_api_v1',  'weather_api_v1', url_prefix='/api/v1/weather')

crime_api_v1 = Blueprint(
    'crime_api_v1',  'crime_api_v1',  url_prefix='/api/v1/crime' )


@weather_api_v1.route('/all', methods=['GET'])
def api_search_weather():

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

@crime_api_v1.route('/filtered', methods=['GET'])
def api_get_filtered_crimes():
    filters = {"fields": ["geometry", "properties.START_DATE", "properties.LATITUDE", "properties.LONGITUDE", "properties.OFFENSE"]}
    (crimes, total_num_entries) = get_crimes(filters)

    response = {
        "total_results": total_num_entries,
        "filters": filters,
        "crimes": crimes,
    }

    page_sanitized = json.loads(json_util.dumps(response))
    return page_sanitized
