# Copyright (c) 2021 ayupy
# This software is released under the MIT License, see LICENSE.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
    
