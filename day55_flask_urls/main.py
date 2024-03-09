from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hello.html')


@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"<p>Hello {name}! You are {number} years old!</p>"

# 



# to run whithout using cmd >flask --app <filename> run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run(debug=True)