set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py makemigrations api
python manage.py migrate api

python manage.py makemigrations
python manage.py migrate