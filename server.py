from flask import Flask
from flask import render_template, redirect, url_for
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

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/tips/1_1')
def tip1_1():
   return render_template('tips/tip1_1.html')

@app.route('/tips/annotated_tip1_1')
def red_tip1_1():
   return render_template('red_tips/red_tip1_1.html')

@app.route('/tips/1_2')
def tip1_2():
   return render_template('tips/tip1_2.html')

@app.route('/tips/annotated_tip1_2')
def red_tip1_2():
   return render_template('red_tips/red_tip1_2.html')

@app.route('/tips/2_1')
def tip2_1():
   return render_template('tips/tip2_1.html')

@app.route('/tips/annotated_tip2_1')
def red_tip2_1():
   return render_template('red_tips/red_tip2_1.html')

@app.route('/tips/2_2')
def tip2_2():
   return render_template('tips/tip2_2.html')

@app.route('/tips/annotated_tip2_2')
def red_tip2_2():
   return render_template('red_tips/red_tip2_2.html')

@app.route('/tips/3_1')
def tip3_1():
   return render_template('tips/tip3_1.html')

@app.route('/tips/annotated_tip3_1')
def red_tip3_1():
   return render_template('red_tips/red_tip3_1.html')

@app.route('/tips/3_2')
def tip3_2():
   return render_template('tips/tip3_2.html')

@app.route('/tips/annotated_tip3_2')
def red_tip3_2():
   return render_template('red_tips/red_tip3_2.html')

@app.route('/tips/4_1')
def tip4_1():
   return render_template('tips/tip4_1.html')

@app.route('/tips/annotated_tip4_1')
def red_tip4_1():
   return render_template('red_tips/red_tip4_1.html')

@app.route('/tips/4_2')
def tip4_2():
   return render_template('tips/tip4_2.html')

@app.route('/tips/annotated_tip4_2')
def red_tip4_2():
   return render_template('red_tips/red_tip4_2.html')

@app.route('/tips/5_1')
def tip5_1():
   return render_template('tips/tip5_1.html')

@app.route('/tips/5_2')
def tip5_2():
   return render_template('tips/tip5_2.html')

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
      return redirect(url_for('finish_quiz'))

@app.route('/quiz/finish')
def finish_quiz():
   return render_template('quiz/quiz-complete.html', score=quiz_score, total=quiz_total)

@app.route('/quiz/<number>/correct')
def correct_quiz(number=None):
   index = int(number) - 1
   return render_template('quiz/correct_quiz.html', file=quiz_data[index])

@app.route('/quiz/<number>/incorrect')
def incorrect_quiz(number=None):
   index = int(number) - 1
   return render_template('quiz/incorrect_quiz.html', file=quiz_data[index])

@app.route('/increment_score', methods=['POST'])
def increment_score():
    global quiz_score
    quiz_score += 1

if __name__ == '__main__':
   app.run(debug = True, port=4444)

