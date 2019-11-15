from wtforms import StringField, SubmitField, FileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class AddProduct(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpeg', 'jpg', 'png'])])
    submit = SubmitField('Add')
