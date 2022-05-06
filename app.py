from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/my_page')
def my_page():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
