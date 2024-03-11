from flask import Flask,render_template
import random, time, requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(0,9)
    current_time = time.localtime()
    current_year = current_time.tm_year 
    return render_template("index.html",num=random_number, year=current_year)


@app.route("/guess/<user_name>")
def guess(user_name):
    params = {
        "name": user_name
    }
    response = requests.get("https://api.genderize.io",params=params)
    gender = response.json()["gender"]
    response = requests.get("https://api.agify.io",params=params)
    age = response.json()["age"]
    return render_template('guess.html',gender=gender,age=age)


# to run whithout using cmd >flask --app <filename> run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run(debug=True)