Установка:
git clone https://github.com/artbotguy/my-web-pet.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Добавление/удаление пакетов:
pip install/uninstall <package>
pip freeze > requirements.txt




alias gustart='gunicorn -w 4 -b 0.0.0.0:5000 app:app > /dev/null 2>&1 &'
alias gustop='pkill -f "gunicorn"'

alias gustartv='gunicorn -w 4 -b 0.0.0.0:5000 app:app'



TODO

Для постоянной работы создаем Systemd-сервис:

bash
sudo nano /etc/systemd/system/myflaskapp.service
Конфиг сервиса:

ini
[Unit]
Description=Gunicorn для моего Flask-приложения
After=network.target

[Service]
User=ваш_пользователь  # Например, ubuntu
WorkingDirectory=/путь/к/вашему/приложению
ExecStart=/путь/к/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
Запускаем сервис:

bash
sudo systemctl daemon-reload
