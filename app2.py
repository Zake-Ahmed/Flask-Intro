from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/square/<int:num>')
def square(num):
    return f'{num} squared is {num**2}'

@app.route('/factorial/<int:num>')
def fact(num):
    x=1
    for i in range(1,num+1):
        x *=i
    
    return f'{num} factorial is  {x}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)