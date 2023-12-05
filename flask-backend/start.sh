#/bin/bash

. .venv/bin/activate
flask --app app run --reload --host=0.0.0.0
