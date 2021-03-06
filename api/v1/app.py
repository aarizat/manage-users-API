
'''
Run app.
'''
from os import getenv

from flask import Flask

from api.v1.extensions import db
from api.v1.config import Config
from api.v1.models.user import User


app = Flask(__name__)
app.config.from_object(Config)

# init database
db.init_app(app)
with app.app_context():
    db.create_all()

# register blueprint
from api.v1.views import app_views
app.register_blueprint(app_views)

if __name__ == '__main__':
    app.run(host=getenv('API_HOST'), port=getenv('API_PORT'))
