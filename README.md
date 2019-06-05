# UploadImages

Полностью совпадает с условиями в ТЗ.

Для корректной работы, нужно в URL вставлять изображения с адресом похожим на:

https://example.com/example.jpg

или

https://example.com/example.png

Для запуска использовать команду

        python3 manage.py runserver


#Способ деплоя:


ПЕРВИЧНАЯ НАСТРОЙКА СЕРВЕРА

Установка пакетов

        sudo apt update
        sudo apt upgrade
        sudo apt install nano
        sudo apt install git python3 python3-dev
        sudo apt install make
        sudo apt install mysql-server
        sudo apt install virtualenv
        sudo apt install build-essential
        sudo apt install libmysqlclient-dev

ПОЛУЧЕНИЕ ИСХОДНИКОВ

        ssh-keygen-t rsa–C "your@email.com"
        #добавить публичный ключ в git
        git clone git@server.com:repo 
        cd repo

   Настройка virtualenv
    
        virtualenv -p python3 venv
        source ~/repo/venv/bin/activate
        (venv) pip install -r requirements.txt
    
   ПРОБНЫЙ ЗАПУСК
   
   DEBUG = False
   
   ALLOWED_HOSTS = ["yourdomain.tk"]
   
        Запуск
        (venv) python manage.py migrate
        (venv) python manage.py runserver0.0.0.0:8000
       
Дальше происходит настройка БД

После настройки нужно установить gunicorn
        
        pip install gunicorn
        sudonano/etc/systemd/system/gunicorn.service 
       
Проверка и запуск сервиса

        sudo systemctl daemon-reload    
        sudo systemctl start gunicorn
        sudo systemctl enable gunicorn
        sudo systemctl status gunicorn