Three things are most important for simple web
setting.py --> Enter the added added app name : rage_app
views.py --> add the functions 
urls.py --> add the url path and functions

4 files more important for db connective work:
models.py
admin.py
migration directory
db.sqlite 

step1: check db using following command
#python manage.py db.shell
sqlite>> .tables --> list the tables
sqlite>> select * from "tables name" --> list the data
sqlite>> .exit


create one more app for db work or added work (eg. meeting)

add app name in to setting.py

model.py --> import module
             class meeting():
             char,inter,data,time field add. CASE SENSITVE MANDATORY CHECK

admin.py --> from .models import meeting
             admin.site.register(meeting)


#python manage.py makemigrations --> if you got error 1 and 2 option. delete the unwanted file in migration folder
#python manage.py migrate 

#python manage.py createsuperuser --> usercreate

#python manage.py runserver

127.0.0.1:8000/admin --> login and work
