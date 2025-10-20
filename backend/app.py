from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../frontend', static_url_path='/')
    app.config.from_object(config_class)
    CORS(app)
    db.init_app(app)

    from routes.comments import bp as comments_bp
    from routes.tasks import bp as tasks_bp
    app.register_blueprint(comments_bp)
    app.register_blueprint(tasks_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
