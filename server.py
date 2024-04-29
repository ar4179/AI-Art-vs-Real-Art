from flask import Flask
from flask import render_template
from flask import Response, request
from flask import jsonify
import threading
from markupsafe import escape
import json

app = Flask(__name__)

# used for changing color of the link corresponding to current page in navbar
def is_active(path):
    if request.path.startswith(path):
       return 'active' 
    else: 
       ''

@app.context_processor
def context_processor():
    return dict(is_active=is_active)

# Thread-safe dictionary to store the durations
user_durations = threading.Lock()
page_times = {}

@app.route('/update_time', methods=['POST'])
def update_time():
   if request.method == 'POST':
      data = request.get_json()
      
      page = data['page']
      duration = data['duration']

      with user_durations:
         if page in page_times:
            page_times[page] += duration
         else:
            page_times[page] = duration

      print(page_times)
      return jsonify({"status": "success", "updated_time": page_times[page]})

def read_data():
   with open('static/quiz_pictures.json', 'r') as file:
      return json.load(file)
   
quiz_data = read_data()
quiz_score = 0
quiz_total = len(quiz_data)

# to protect from injection attacks
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/home')
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

@app.route('/quiz/start')
def start_quiz():
   global quiz_score
   quiz_score = 0
   return render_template('quiz/start_quiz.html')

@app.route('/quiz/<number>')
def quiz(number=None):
   index = int(number) - 1
   if 0 <= index < len(quiz_data):
      return render_template('quiz/quiz.html', file=quiz_data[index])
   else:
      return render_template('quiz/quiz-complete.html', score=quiz_score, total=quiz_total)

@app.route('/quiz/<number>/correct')
def correct_quiz(number=None):
   global quiz_score
   quiz_score = quiz_score + 1
   index = int(number) - 1
   return render_template('quiz/correct_quiz.html', file=quiz_data[index])

@app.route('/quiz/<number>/incorrect')
def incorrect_quiz(number=None):
   index = int(number) - 1
   return render_template('quiz/incorrect_quiz.html', file=quiz_data[index])


if __name__ == '__main__':
   app.run(debug = True, port=4444)

