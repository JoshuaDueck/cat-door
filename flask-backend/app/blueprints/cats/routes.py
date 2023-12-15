from app.blueprints.cats import bp


@bp.route('/', methods=['GET'])
def index():
    return 'cats root'


@bp.route('/', methods=['POST'])
def create_cat():
    return 'create cat'


@bp.route('/<int:cat_id>', methods=['GET'])
def get_cat(cat_id):
    return 'cat {}'.format(cat_id)


@bp.route('/<int:cat_id>', methods=['POST'])
def edit_cat(cat_id):
    return 'cat {}'.format(cat_id)


@bp.route('/<int:cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    return 'cat {} deleted'.format(cat_id)


@bp.route('/byRfid/<int:cat_rfid>', methods=['GET'])
def get_cat_by_rfid(cat_rfid):
    return 'cat {}'.format(cat_rfid)
