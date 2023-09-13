from flask import Flask, render_template,request
from aiAnswer import getAnswer
import source.download as downTokenizer
app = Flask(__name__, template_folder="templates",static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/reply',methods=['POST'])
def reply():
    data=request.get_json()
    question=data.get('question')
    reply=getAnswer(question)
    return {'reply':reply}

if __name__ == '__main__':
    #downTokenizer.isdown()
    app.run()