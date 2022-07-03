from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_em():
        return "<em>" + function() + "</em>"
    return wrapper_em

def make_underlined(function):
    def wrapper_U():
        return "<u>" + function() + "</u>"
    return wrapper_U

@app.route("/bye")
@make_underlined
def bye():
    return 'bye'

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media2.giphy.com/media/4VglqgTazN7YQ/200w.webp?cid=ecf05e47lullv0h8rbmn9pzjpdfddsxug845ssb4obc50mt3&rid=200w.webp&ct=g">'

@app.route("/user/<name>")
def greeting(name):
    return f"Hello {name}"

#Creating variable paths and converting the path to a specified data type
@app.route("/user/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)