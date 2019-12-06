#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 19-11-29.
# email to LipsonChan@yahoo.com
#


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
