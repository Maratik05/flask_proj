from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return 'Hello world'

@app.route('/<name>/')
def index2(name):
    text = 'Hello {{ name }}'
    return f'Hello {name}'

@app.route('/page/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
