from flask import Flask, render_template, request
from threading import Thread
from info import info

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/info')
def infoo():
    return render_template("info.html")


def run():
    app.run(host='0.0.0.0')


def show_site():
    t = Thread(target=run)
    t.start()


run()
