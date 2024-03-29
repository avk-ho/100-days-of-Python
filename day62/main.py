from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField("Cafe location on Google Maps (url)", validators=[DataRequired(), URL()])
    open_time = StringField("Opening time (ex: 8:30AM)", validators=[DataRequired()])
    closing_time = StringField(
        "Closing time (ex: 11:45PM", validators=[DataRequired()])
    coffee = SelectField(label="Coffee rating", validators=[DataRequired()],
        choices=[
            ("✘", "✘"),
            ("☕️", "☕️"),
            ("☕️☕️", "☕️☕️"),
            ("☕️☕️☕️", "☕️☕️☕️"),
            ("☕️☕️☕️☕️", "☕️☕️☕️☕️"),
            ("☕️☕️☕️☕️☕️", "☕️☕️☕️☕️☕️")
        ]
    )
    wifi = SelectField(label="Wifi strength rating", validators=[DataRequired()], 
        choices=[
            ("✘", "✘"),
            ("💪", "💪"),
            ("💪💪", "💪💪"),
            ("💪💪💪", "💪💪💪"),
            ("💪💪💪💪", "💪💪💪💪"),
            ("💪💪💪💪💪", "💪💪💪💪💪")
        ]
    )
    power = SelectField(label="Power outlet rating", validators=[DataRequired()], 
        choices=[
            ("✘", "✘"),
            ("🔌", "🔌"),
            ("🔌🔌", "🔌🔌"),
            ("🔌🔌🔌", "🔌🔌🔌"),
            ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")
        ]
    )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open("day62/cafe-data.csv", "a", encoding="utf8") as csv_file:
            new_data = [
                form.cafe.data, 
                form.location_url.data, 
                form.open_time.data, 
                form.closing_time.data, 
                form.coffee.data, 
                form.wifi.data, 
                form.power.data
            ]
            print(new_data)

            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day62/cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
