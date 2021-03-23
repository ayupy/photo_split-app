# Copyright (c) 2021 ayupy
# This software is released under the MIT License, see LICENSE.

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
    
