from flask import Blueprint, jsonify, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

vegetable = Blueprint('vegetables', __name__, template_folder='template')

vegetables = {
    "veg1": "carrot",
    "veg2": "tomato",
    }


class RegistrationForm(Form):
    username = StringField("Username", [validators.Length(min=6, max=25)])
    email = StringField("Email", [validators.Length(min=6, max=35)])
    # password = PasswordField("New Password", [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message="Passwords must match")
    # ])
    # confirm = PasswordField("Repeat Password")
    # accept_tos = BooleanField("I accept the TOS", [validators.DataRequired()])


@vegetable.route('/vegetable')
def get_vegetable():
    form = RegistrationForm(request.form)
    return jsonify(vegetables)
    # return render_template('main.html')
