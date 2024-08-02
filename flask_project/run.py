from app.factory import create_app
from app import app
import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("sample.ini")))


if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = False
    # app.config['MONGO_URI'] = config['TEST']['DB_URI']
    app.run(debug=True)
