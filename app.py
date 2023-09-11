from flask import Flask, render_template
import webSearch

app = Flask(__name__, template_folder="templates",static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/reply',methods=['POST'])
def reply():
    reply="你好！"
    return {'reply': reply}

if __name__ == '__main__':
    app.run()