from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    # Конфигурация
    app.config['UPLOAD_FOLDER'] = os.path.join(
        os.path.dirname(__file__), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # Создаем папку для загрузок
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import bp
    app.register_blueprint(bp)

    return app
