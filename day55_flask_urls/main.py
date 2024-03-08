from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"<p>Hello {name}! You are {number} years old!</p>"



# to run whithout using cmd >flask --app <filename> run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run(debug=True)