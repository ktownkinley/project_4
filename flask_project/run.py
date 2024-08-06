from app.factory import create_app
from app import app
import configparser

config = configparser.ConfigParser()

# test config
if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.run(debug=True)


# prod config
# if __name__ == "__main__":
#     app = create_app()
#     app.config['DEBUG'] = False
#     app.run(host="0.0.0.0", port=5000)
