pip install django
pip install mysqlclient #(brew install mysql pkg-config)
pip install django-cors-headers


cut -d',' -f3,5,8,9,19 original.csv > pp_data.csv

python manage.py load_data