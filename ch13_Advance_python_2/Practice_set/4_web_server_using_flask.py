from flask import Flask

#flask is used to create websites and APIs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is jayshree.</p>"

app.run()