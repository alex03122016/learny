import flask
from flask import Flask #originial
#from flask_shelve import init_app
import os
app = Flask(__name__)#original





#app.config['SHELVE_FILENAME'] = os.path.join(os.path.expanduser('~'), 'microblog','app', 'dictdata')
#app.config['SHELVE_LOCKFILE'] = os.path.join(os.path.expanduser('~'), 'microblog','app', 'dictdata' + '.lock')
#app.config['SHELVE_FILENAME'] = 'dictdata'
#init_app(app)





from app import routes
