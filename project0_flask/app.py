from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/page_1.html')
def page_1():
    return render_template("page_1.html")


@app.route('/page_2.html')
def page_2():
    return render_template("page_2.html")


if __name__ == '__main__':
    app.run()
