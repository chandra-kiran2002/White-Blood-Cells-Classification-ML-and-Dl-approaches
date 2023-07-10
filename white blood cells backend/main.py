from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def inner():
        return "<b>"+function()+"</b>"
    return inner
def make_h1(function):
    def inner():
        return "<h1>"+function()+"</h1>"
    return inner
@app.route('/')
@make_bold
@make_h1
def hello_world():
    return "hello world"

if __name__=="__main__":
    app.run(debug=True)