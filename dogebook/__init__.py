from flask import Flask 
from dogebook.config import configurations

def create_app(environment_name='dev'):
	app = Flask(__name__)
	app.config.from_object(configurations[environment_name])
	return app

