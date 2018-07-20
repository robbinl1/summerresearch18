from flask import Flask

appFlask = Flask(__name__)
appFlask.config['SECRET_KEY'] = 'something-super-secret' #This is necessary for working with forms

from appfolder import routes

