import os
# from app import app  #Import the app variable inside our app directory
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Import colorization algorithm
from colorization_algorithms.colorization_master import demo_release

app = Flask(__name__)

# Disable Cache - Allows saving file in same name and display it right away
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# SECRET KEY
# Resource: https://stackoverflow.com/questions/27287391/why-not-generate-the-secret-key-every-time-flask-starts
secret_key='dsjiofh3289usfdjhf34789'  # Make your own secret key
app.secret_key = bytes(secret_key, 'utf-8')
# app.config.update(SECRET_KEY=secret_key)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set file size limit to 16 megabytes (raise RequestEntityTooLarge exception if file limit exceeded)
app.config['UPLOAD_FOLDER'] = 'static/img/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp'}

# @app.route("/", methods=["POST", "GET"])
# def home():  
#     if request.method == "POST":
#         user = request.form["file_path"]
#         return redirect(url_for("result"))  # << Replace this with coloration func?
#     else:
#      return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Hint: Try landscapes and portraits for amazing results!')
            return render_template('index.html', filename=filename)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, webp')
            return redirect(request.url)
    else:
        return render_template('index.html')


@app.route('/result/<filename>')
def display_result(filename):
    """Display/embed image on website"""
    filepath = 'static/img/uploads/' + filename
    model_dir = 'colorization_algorithms/colorization_master/models'
    demo_release.main(filepath, model_dir)
    return redirect(url_for('static', filename='img/results_img/saved_result_final.png'), code=307)
    # return redirect(url_for('static', filename='img/uploads/' + filename))


@app.route('/about')
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
    app.run(debug=True)