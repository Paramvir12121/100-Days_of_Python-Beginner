from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye</p>"


# to run whithout using cmd >flask --app hello run 
# Allows to just use python hello.py
if __name__ == "__main__":
    app.run()