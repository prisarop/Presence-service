# Presence-service
1. Install django
2. Install djangorestfamework
3. Install PostgreSQL
4. Install pgadmin
5. Go to the setting.py and see the section of databases then see the password of database.
6. Go PostgreSQL create database with name dochub then run command "./mange.py runserver" on your ide terminal if it shows some error then
    run this command "python manage.py makemigration" then it will show "0001 initial.py" after it run the command "python manage.py 
    sqlmigrate dochub 0001" then run "python manage.py makemigrate".
7. Even after that program doesn't run then run above command with put 0002 in place of 0001.
8. Now you are done.
