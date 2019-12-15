rm -v tumblr/migrations/0*
mysql -u root --password=adminadmin < restart_db.sql
python manage.py makemigrations
python manage.py migrate