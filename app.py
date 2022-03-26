from flask import Flask, render_template
from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "temp secret key"


# Form class
class Form(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():  # put application's code here
    first_name = "Seth"
    stuff = "This is bold text."
    favorites = ["Pizza", "Hot Dogs", 42]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorites=favorites)


@app.route('/user/<name>')
def user(name):  # put application's code here
    return render_template("user.html", user_name=name)


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('name.html', name=name, form=form)



if __name__ == '__main__':
    app.run()
