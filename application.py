import os
# from app import app  #Import the app variable inside our app directory
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Import colorization algorithm
from colorization_algorithms import colorizer
from form import PhotoForm

application = Flask(__name__)

# Config
# NEED TO RUN: export APP_SETTINGS="config...." - before running program for now (I will automate this later)
# application.config.from_object(os.environ["APP_SETTINGS"])
application.config.from_object("config.ProductionConfig")
sitekey = application.config['RECAPTCHA_PUBLIC_KEY']


@application.route('/', methods=['GET', 'POST'])
def home():
    form = PhotoForm()

    if request.method == 'POST' and form.validate_on_submit():
        f = form.photo.data
        # filename = secure_filename(f.filename)
        filename = "uploaded_img.jpg"
        f.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        flash('Hint: Try landscapes and portraits for amazing results!')

        return render_template('index.html', filename=filename, form=form, sitekey=sitekey)
        # return redirect(url_for('index.html'))
    else:
        return render_template('index.html', form=form)


@application.route('/result/<filename>')
def display_result(filename):
    """Display/embed image on website"""
    filepath = application.config['UPLOAD_FOLDER'] + filename
    model_dir = application.config['MODEL_FOLDER']
    colorizer.main(filepath, model_dir)
    return redirect(url_for('static', filename='img/results_img/saved_result_final.png'), code=307)
    # return redirect(url_for('static', filename='img/uploads/' + filename))


@application.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    application.run()