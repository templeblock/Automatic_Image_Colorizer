from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, validators


class PhotoForm(FlaskForm):
    recaptcha = RecaptchaField()
    photo = FileField("File", validators=[
        FileRequired('No file selected for uploading'),
        FileAllowed(['png', 'jpg', 'jpeg', 'webp'], 'Allowed image types are -> png, jpg, jpeg, webp')])
    submit = SubmitField('Submit')
