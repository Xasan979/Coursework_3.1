from flask import Flask

from app.main.views import pages_blueprint
from app.errors.views import error_pages_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(pages_blueprint)
app.register_blueprint(error_pages_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(debug=True)