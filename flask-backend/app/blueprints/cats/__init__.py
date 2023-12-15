from flask import Blueprint

bp = Blueprint('cats', __name__, url_prefix='/api/v1/cats')

from app.blueprints.cats import routes  # noqa, isort:skip
