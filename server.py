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

@app.route('/tips/1')
def tip1():
   return render_template('tips/tip1.html')

@app.route('/tips/annotated_tip1')
def red_tip1():
   return render_template('red_tips/red_tip1.html')

@app.route('/tips/2')
def tip2():
   return render_template('tips/tip2.html')

@app.route('/tips/annotated_tip2')
def red_tip2():
   return render_template('red_tips/red_tip2.html')

@app.route('/tips/3')
def tip3():
   return render_template('tips/tip3.html')

@app.route('/tips/annotated_tip3')
def red_tip3():
   return render_template('red_tips/red_tip3.html')

@app.route('/tips/4')
def tip4():
   return render_template('tips/tip4.html')

@app.route('/tips/annotated_tip4')
def red_tip4():
   return render_template('red_tips/red_tip4.html')

@app.route('/tips/5')
def tip5():
   return render_template('tips/tip5.html')


if __name__ == '__main__':
   app.run(debug = True, port=4444)

