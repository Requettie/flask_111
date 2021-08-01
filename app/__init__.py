#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple flask app"""

from flask import Flask

app = Flask(__name__) #__name__ is a dunder variable or "magic variable"

@app.route("/")
def about_me():
    me = {
        "first_name": "Reese",
        "last_name": "Gick",
        "hobbies": "DIY stuff"
        
    }
    return me