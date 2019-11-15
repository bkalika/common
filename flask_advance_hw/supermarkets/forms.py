from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired


class AddSupermarket(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpeg', 'jpg', 'png'])])
    submit = SubmitField('Add')
