from app.blueprints.cats import bp


@bp.route('/', methods=['GET'])
def index():
    return 'cats root'
