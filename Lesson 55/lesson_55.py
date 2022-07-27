from flask import Flask
from random import randint
app = Flask(__name__)

number = randint(0, 9)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media0.giphy.com/media/IsfrRWvbUdRny/200w.webp?cid=ecf05e47b3u1tims1al0mltpvg7eb1o4237nmq6f9d790kbr&rid=200w.webp&ct=g">'

@app.route(f'/{number}')
def right_guess():
    return '<img src="https://media2.giphy.com/media/3oFzmkkwfOGlzZ0gxi/200w.webp?cid=ecf05e47de8wk33cmz6963di7e5lzstu6m2a6e1b0vze209s&rid=200w.webp&ct=g">'

@app.route('/<int:guess>')
def wrong_guess(guess):
    if guess > number:
        return '<h1>too high</h1>'
    elif guess < number:
        return '<h1>too low</h1>'

if __name__ == '__main__':
    app.run(debug=True)
