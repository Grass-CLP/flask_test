#!/usr/bin/env bash

~/anaconda2/envs/flask_test/bin/alembic revision --autogenerate -m "first"
~/anaconda2/envs/flask_test/bin/alembic upgrade head