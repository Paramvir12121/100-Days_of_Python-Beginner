from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(0,9)
    return render_template("index.html",num=random_number)


# to run whithout using cmd >flask --app <filename> run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run(debug=True)