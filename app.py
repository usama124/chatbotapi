from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
# from flask_restplus import Api

import settings as app_settings
# from configs import Config, JsonEncoder
from models import *
from views import auth_api, listfiles_api, about_api, addtag_api, createfile_api, editfile_api, readfile_api, trainmodel_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = app_settings.DATABASE_URI
db.init_app(app)
CORS(app)
# api = Api(app, prefix='/api/v1')
migrate = Migrate(app, db)

app.register_blueprint(about_api.blueprint)
app.register_blueprint(auth_api.blueprint)
app.register_blueprint(listfiles_api.blueprint)
# app.register_blueprint(addtag_api.blueprint)
# app.register_blueprint(createfile_api.blueprint)
app.register_blueprint(readfile_api.blueprint)
# app.register_blueprint(editfile_api.blueprint)
# app.register_blueprint(trainmodel_api.blueprint)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5006)