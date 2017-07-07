from flask import Flask
import sys
import os

app = None
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys.executable, '..', 'templates')
    static_folder = os.path.join(sys.executable, '..', 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

from application.views import index
