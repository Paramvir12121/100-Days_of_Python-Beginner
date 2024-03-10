from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def hello_world():
    return render_template('hello.html')


@app.route("/hilo/<int:guess>")
def greet(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


# to run whithout using cmd >flask --app <filename> run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run(debug=True)