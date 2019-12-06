#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 19-11-29.
# email to LipsonChan@yahoo.com
#


from flask_test import create_app
# from flaskr.db import init_db

if __name__ == "__main__":
    app = create_app()
    # init_db()
    app.run()
