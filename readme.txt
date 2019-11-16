Steps to use MySQL instead of SQLite:

If you want to keep all your information, follow this steps, if not, jump directly to 'Now, donwload the ...'. 

First, in the settings.py file, uncomment the DATABASES dictionary that contains the sqlite3 database and comment the one with the mysql database. 

Then, go to the PracticaWeb directory and run 'python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > datadump.json'. This will generate a datadump.json that will upload the data currently in our database to the new one. 

Then, recomment the one with the sqlite3 and uncomment the one with the mysql.

Now, download the MySQL Program (server) from their website. Then, run the installation program and define the password of the root user: 'adminadmin', then create a database called 'dumblr'. After the installation, run in a terminal 'pip install pymysql'.

Once all of that is done, try to run 'python manage.py migrate'. If that does not fail, then simply run 'python manage.py loaddata datadump.json' to load all the data that the database had before.