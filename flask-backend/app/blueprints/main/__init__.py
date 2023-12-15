from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/api/v1')

from app.blueprints.main import routes  # noqa, isort:skip
