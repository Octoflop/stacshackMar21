import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from predictor import Predictor
import uuid

FOLDER = 'static/upload'
ALLOWED = {'jpg','png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER
app.config['PREDICTOR'] = Predictor()

@app.route('/', methods=['GET','POST'])
def file_upload():
    report = ''
    if (request.method == 'POST'):
        uploaded = request.files['file']
        filename = str(uuid.uuid4()) + '.png'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded.save(filepath)
        verdict = app.config['PREDICTOR'].do_prediction(filepath)

        if (verdict != 1):
            report = 'Not a hedgehog, better luck next time!'
        else :
            report = 'Looks like you\'ve got a hedgehog there pal!'
        
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', report=report, images=images)


if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)


