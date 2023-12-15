from app.blueprints.main import bp


@bp.route('/')
def index():
    return "Main Blueprint Root Path"


@bp.route('/door', methods=['GET'])
def get_door():
    return "Main Blueprint Door Path"


@bp.route('/door/unlock', methods=['POST'])
def unlock_door():
    return "Main Blueprint Door Unlock Path"


@bp.route('/door/lock', methods=['POST'])
def lock_door():
    return "Main Blueprint Door Lock Path"
