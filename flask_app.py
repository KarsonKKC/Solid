from re import A
from flask import Flask
import requests
from rhino3dm import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Karson from UNSW CODE!'


def game_1():
    fill = input("A Word: ")
    fill_again = input("Another Word: ")

    madlib = f"Computer programming is so {fill}! It makes me so excited all the time because I love to {fill_again}!"
    print(madlib)
