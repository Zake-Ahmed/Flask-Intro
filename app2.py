from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/home/<int:num>')
def square(num):
    return f'{num} squared is {num**2}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)