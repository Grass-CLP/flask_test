#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 19-11-29.
# email to LipsonChan@yahoo.com
#


from gevent.pywsgi import WSGIServer
from hello import app
from flaskr import create_app

http_server = WSGIServer(('', 5000), create_app())
http_server.serve_forever()
