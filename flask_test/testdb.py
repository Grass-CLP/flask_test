#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 19-12-2.
# email to LipsonChan@yahoo.com
#
from flask_test.orms import User, db

u = db.query(User).filter(User.name == 'a').first()
