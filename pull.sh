#!/bin/bash

branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')

git checkout master
git pull origin master
git checkout $branch
cd flask-backend
. .venv/bin/activate
flask db upgrade
deactivate
