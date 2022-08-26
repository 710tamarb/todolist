from crypt import METHOD_BLOWFISH
from flask import Flask, request, Response
import json
import helper

app = Flask(__name__)

@app.route('/item/new', METHOD=['POST'])
def add_item():
    pass