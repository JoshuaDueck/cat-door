from flask import Flask

from config import Config
from app.extensions import db, migrate

from app.models.cat import Cat
from app.models.log_entry import LogEntry


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # EXTENSIONS
    db.init_app(app)
    migrate.init_app(app, db)

    # BLUEPRINTS
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.cats import bp as cats_bp
    app.register_blueprint(cats_bp)

    from app.blueprints.log_entries import bp as log_entries_bp
    app.register_blueprint(log_entries_bp)

    return app
