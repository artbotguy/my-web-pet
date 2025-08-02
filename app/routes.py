from flask import Blueprint, render_template, request, current_app
from .utils.file_upload import FileUploader  # Импортируем класс

bp = Blueprint('main', __name__)
uploader = FileUploader()


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/test')
def test():
    return render_template('test.html')


@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', message='Файл не выбран')

        file = request.files['file']
        filename, error = uploader.save_file(
            file, current_app.config['UPLOAD_FOLDER'])

        if error:
            return render_template('upload.html', message=error)

        file_url = f"/uploads/{filename}"
        return render_template('upload.html',
                               message=f'Файл загружен: <a href="{file_url}">{filename}</a>')

    return render_template('upload.html')
