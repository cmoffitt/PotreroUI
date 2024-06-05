from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World from Potrero!</p>"

@app.route("/image") 
def serve_image(): 
    return render_template('image.html')