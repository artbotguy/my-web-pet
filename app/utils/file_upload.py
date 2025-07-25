import os
from werkzeug.utils import secure_filename
import uuid


class FileUploader:
    def __init__(self):
        self.allowed_extensions = {'txt', 'pdf',
                                   'png', 'jpg', 'jpeg', 'gif', 'bin'}

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def generate_filename(self, original_filename):
        ext = os.path.splitext(original_filename)[1]
        return f"{uuid.uuid4()}{ext}"

    def save_file(self, file, upload_folder):
        if not file or file.filename == '':
            return None, "Файл не выбран"

        if not self.allowed_file(file.filename):
            return None, "Недопустимый тип файла"

        filename = self.generate_filename(secure_filename(file.filename))
        save_path = os.path.join(upload_folder, filename)

        try:
            file.save(save_path)
            return filename, None
        except Exception as e:
            return None, f"Ошибка при сохранении: {str(e)}"


# Создаем экземпляр для импорта
uploader = FileUploader()
