from flask import Blueprint

bp = Blueprint('log_entries', __name__, url_prefix='/api/v1/log_entries')

from app.blueprints.log_entries import routes  # noqa, isort:skip
