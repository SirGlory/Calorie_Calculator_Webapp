from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

# Create app instance
app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        age = float(calories_form.age.data)
        height = float(calories_form.height.data)
        weight = float(calories_form.weight.data)
        country = calories_form.country.data
        city = calories_form.city.data

        temperature = Temperature(country=country, city=city).get()
        calories = Calorie(age=age,
                            weight=weight,
                            height=height,
                            temperature=temperature).calculate()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               temperature=temperature,
                               result=True)



class CaloriesForm(Form):
    age = StringField("What is your age? ", default=25)
    height = StringField("What is your height in cm? ", default=185)
    weight = StringField("What is your weight in kg? ", default=80)
    country = StringField("Which country are you in? ", default='Italy')
    city = StringField("Which city are you in? ", default='Rome')
    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
