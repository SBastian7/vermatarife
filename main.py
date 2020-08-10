from flask import Flask, render_template, url_for, session, redirect, request, Response, flash, send_from_directory, send_file
from flask_pymongo import PyMongo, ObjectId

import gridfs   #Imagenes
import bcrypt   #Hash
import ssl
import os
import math

app = Flask(__name__)
app.secret_key = 'jejejeje'
UPLOAD_DIRECTORY = "static/videos/es"
app.config['MONGO_DBNAME'] = 'NOMBRE'
app.config['SECRET_KEY'] = 'SECRETKEY'
app.config['MONGO_URI'] = 'mongodb+srv://admin:utp123@cluster0-tjpda.mongodb.net/test?retryWrites=true&w=majority'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

mongo = PyMongo(app)
fs = gridfs.GridFS(mongo.db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/videos/es/<video>')
def download(video):
    flash(u"Descarga iniciada")
    return send_from_directory(UPLOAD_DIRECTORY, video, as_attachment=True)

@app.route('/pwabuilder-sw.js')
def sw():
    return app.send_static_file('pwabuilder-sw.js')

@app.route('/view/<video>')
def view(video):
    return render_template('view.html',video=video)


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
