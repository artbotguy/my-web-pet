## Важные поинты 
- есть измнения в основной конфиге и локальных, все лежит в ./nginx


## Установка:
git clone https://github.com/artbotguy/my-web-pet.git
cd my-web-pet
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
    # если траблы
    cd /var/www/abotkin.space/my-web-pet/
    rm -rf venv
    python3 -m venv venv --clear
    source venv/bin/activate
#### Добавление/удаление пакетов:
pip install/uninstall <package>
pip freeze > requirements.txt
#### Для логов
sudo apt install libnginx-mod-http-headers-more-filter
### Автозапуск
sudo vim /etc/systemd/system/mwp.service #/Users/abotkin/work/my-web-pet/any_serv_files
sudo systemctl daemon-reload 
sudo systemctl enable mwp.service
sudo systemctl start mwp.service

### Запуск приложения вручную
cd /var/www/abotkin.space/my-web-pet/
source venv/bin/activate
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app


### Все команды на запуск/остановку
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app > /dev/null 2>&1 &
pkill -f "gunicorn
|
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

### Команды
    # Логи
    tail -f /var/log/nginx/abotkin.access.log
    tail -f /var/log/nginx/abotkin.error.log
    
    # nginx
    sudo nginx -t && sudo systemctl reload nginx


## TODO



## Optional

### в .bashrc
alias gustart='gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app > /dev/null 2>&1 &'
alias gustop='pkill -f "gunicorn"'
|
alias gustartv='gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app'