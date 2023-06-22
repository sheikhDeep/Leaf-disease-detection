from flask import Flask, render_template, request, redirect, url_for
import requests
from PIL import Image
import json
from werkzeug.utils import secure_filename
import os
from fastai.vision.all import load_learner
from fastai import *
import torch
import pathlib
import pandas as pd


app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            print(filename)
            image.save(f'{UPLOAD_FOLDER}{filename}')

            x, y = result(f'{UPLOAD_FOLDER}{filename}')

            return render_template('home_page.html', label=x, value=y, image=f'upload/{filename}')
        return render_template('home_page.html', label='', value='', image='')
    else:
        return render_template('home_page.html', label='', value='', image='')


def result(path):
    model_path = './multi_target_resnet18.pkl'
    model = load_learner(model_path)
    pred, _, probability = model.predict(path)
    arr = ['Name', 'Status', 'Disease Name']
    vals = ['', '', '']

    names = ['Maple', 'Banana', 'Cucumber',
             'Mango', 'Pepper', 'Rose', 'Tomato']
    status = ['diseased', 'no disease found']

    for x in pred:
        if x in names:
            vals[0] = x.capitalize()
        elif x in status:
            vals[1] = x.capitalize()
        elif x == 'healthy':
            vals[2] = 'None'
        else:
            vals[2] = x.capitalize()

    return arr, vals


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()
