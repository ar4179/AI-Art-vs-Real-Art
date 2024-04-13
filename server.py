from flask import Flask
from flask import render_template
from flask import Response, request
from markupsafe import escape

app = Flask(__name__)

# to protect from injection attacks
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
def home():
   return render_template('homepage.html')

if __name__ == '__main__':
   app.run(debug = True)

