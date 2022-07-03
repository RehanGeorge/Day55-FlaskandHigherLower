from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

number = random.randint(1,10)

@app.route('/<int:ranno>')
def print(ranno):
    if ranno < number:
        return "<h1>Your guess is too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif ranno > number:
        return "<h2>Your guess is too high</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif ranno == number:
        return "<h3>You got it right</h3>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"