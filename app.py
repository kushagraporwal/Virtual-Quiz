from flask import Flask, render_template, get_flashed_messages
from quiz import returnscore
from quiz3 import returnscore2
from quiz4 import returnscore3
import subprocess

app = Flask(__name__)
global score1
global score2
global score3
score1= -1
score2= -1
score3= -1

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/quiz1')
def run_script():
   score1= returnscore()  
   return render_template('index.html', score1=score1, score2=score2, score3=score3)

@app.route('/quiz2')
def run_script2():
   score2= returnscore2()
   return render_template('index.html', score1=score1, score2=score2, score3=score3)

@app.route('/quiz3')
def run_script3():
   score3= returnscore3()
   return render_template('index.html', score1=score1, score2=score2, score3=score3)

if __name__=='__main__':
    app.run(debug=True)