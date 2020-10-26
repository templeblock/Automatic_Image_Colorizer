import os
# from app import app  #Import the app variable inside our app directory
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Import colorization algorithm
from colorization_algorithms import demo_release

application = Flask(__name__)

# Config
# NEED TO RUN: export APP_SETTINGS="config...." - before running program for now (I will automate this later)
# application.config.from_object(os.environ["APP_SETTINGS"])
application.config.from_object("config.BaseConfig")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in application.config['ALLOWED_EXTENSIONS']

@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No image part')
            return redirect(request.url)

        # Save the submitted image into 'file'
        file = request.files['image']  #request.files: storage obj containing files coming in from the form. Access storage by name you gave the file in html: ['image']

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        # If valid file, call uploaded_file():
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            filename = "uploaded_img.jpg"
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            flash('Hint: Try landscapes and portraits for amazing results!')
            return render_template('index.html', filename=filename)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, webp')
            return redirect(request.url)
    else:
        return render_template('index.html')


@application.route('/result/<filename>')
def display_result(filename):
    """Display/embed image on website"""
    filepath = 'static/img/uploads/' + filename
    model_dir = 'colorization_algorithms/models'
    demo_release.main(filepath, model_dir)
    return redirect(url_for('static', filename='img/results_img/saved_result_final.png'), code=307)
    # return redirect(url_for('static', filename='img/uploads/' + filename))


@application.route('/about')
def about():
    return render_template("about.html")

# @app.route('/images/<cropzonekey>')
# def images(cropzonekey):
#     return render_template("images.html", title=cropzonekey)

# @app.route('/fig/<cropzonekey>')
# def fig(cropzonekey):
#     fig = colorization_function(param)
#     img = StringIO()
#     fig.savefig(img)
#     img.seek(0)
#     return send_file(img, mimetype='image/png')


if __name__ == "__main__":
    application.run(debug=True)