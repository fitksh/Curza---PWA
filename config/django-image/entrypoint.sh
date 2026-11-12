#!/usr/bin/env bash
set -euo pipefail

cd /app

if [ ! -f manage.py ]; then
    echo "Creando proyecto Django..."
    django-admin startproject config .
fi

echo "Generando migraciones..."
python manage.py makemigrations --noinput

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Verificando superusuario..."

python manage.py shell <<'PYTHON'
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ["DJANGO_SUPERUSER_USERNAME"]
email = os.environ["DJANGO_SUPERUSER_EMAIL"]
password = os.environ["DJANGO_SUPERUSER_PASSWORD"]

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superusuario creado correctamente.")
else:
    print("El usuario ya existe. No se crea nuevamente.")
PYTHON

echo "Iniciando Django..."

exec python manage.py runserver 0.0.0.0:8000