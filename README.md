# Django Celery Mastery: Python Asynchronous Task Processing

## Install Python

```bash
pyenv install 3.9.5
pyenv global 3.9.5
pip3 install virtualenv
virtualenv env39/ -p python3.9.5
source ~/env39/bin/activate
```

## Install requeriments

```bash
pip3 install django==4.2.2
django-admin startproject dcelery
cd dcelery/
pip install celery==5.3.0
pip install redis==4.5.5

pip freeze > requirements.txt
```

## Deploy with Docker Compose

```bash
docker-compose up -d --build
```