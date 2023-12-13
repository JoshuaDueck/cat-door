from app.blueprints.main import bp


@bp.route('/')
def index():
    return "Main Blueprint Root Path"
