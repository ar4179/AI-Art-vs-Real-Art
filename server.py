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

@app.route('/tip1')
def tip1():
   return render_template('tips/tip1.html')

@app.route('/annotated_tip1')
def red_tip1():
   return render_template('red_tips/red_tip1.html')

@app.route('/tip2')
def tip2():
   return render_template('tips/tip2.html')

@app.route('/annotated_tip2')
def red_tip2():
   return render_template('red_tips/red_tip2.html')

if __name__ == '__main__':
   app.run(debug = True)

