from app.blueprints.cats import bp
from flask import request
from app.models.cat import Cat
from app.extensions import db


@bp.route('/', methods=['GET'])
def index():
    return 'cats root'


@bp.route('/', methods=['POST'])
def create_cat():
    cat_info = request.get_json()

    new_cat = Cat(name=cat_info['name'], rfid=cat_info['rfid'])

    db.session.add(new_cat)
    db.session.commit()

    return (new_cat.__json__(), 200)


@bp.route('/<int:cat_id>', methods=['GET'])
def get_cat(cat_id):
    cat = Cat.query.get(cat_id)
    return (cat.__json__(), 200)


@bp.route('/<int:cat_id>', methods=['POST'])
def edit_cat(cat_id):
    return 'cat {}'.format(cat_id)


@bp.route('/<int:cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    return 'cat {} deleted'.format(cat_id)


@bp.route('/byRfid/<int:cat_rfid>', methods=['GET'])
def get_cat_by_rfid(cat_rfid):
    return 'cat {}'.format(cat_rfid)
