    THESE INSTRUCTIONS ARE FOR LINUX OR MACOS USERS
    
1. create a folder in which you are going to store your files in , navigate using terminal from here on after

2. Installing virtual environment with command :- python -m venv  (myenv). this is the name of the virtual environment created

3. Activate the environment :- source myenv/bin/activate (remember all this should be done in the project directory in terminal)
i) install django (this can be one of your choice i.e pip install django == 3.0.8)

NOTE: 
    installing an older django version is safer and much more stable for the project
    
4. Start project :-  django-admin startproject ......(give a project name of your choice)
        -- also create superuser

5. cd/project

6. Start app :- python manage.py startapp appname....(here your creating an app name for your  project) 

7. migrate :- USE the python manage.py  migrate 

8. runserver :- python manage.py runserver (you can choose a port sever incase you have any active i.e 5050)

9. in the settings.py some versions come with already configured settings while in some one has to add the following
i) UNDER DB
            -- NAME: os.path.join.join(BASE_DIR, dbsqlite3),
ii) TEMPLATES
            -- 'DIRS': [os.path.join(BASE_DIR,"templates"],
iii) BUILD PATHS
            -- BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)
iv) And all installed apps and features like filters can also settle in here 
v) The TEMPLATES setting should be configured with 'APP_DIRS': True to automatically find templates in the app directories.)\
            --the STATICFILES_DIRS also for confinguring static files
            
10.  Create folder called templates
11. Create all html files in the templates folder
         -- create another call STATIC inside the app folder (here you will create css and link those html templates created )
    
12. Now in the app folder create  a  file called views.py in this file you define all the url paths here (this is where urls are defined and redirected)

13. In urls.py (of the app files) :- one has to import django urls and also templates files created i.e urls.py using include().

14. In the main urls.py file one can import the folder into which the templates files are in using :- from django.urls import include.

15. Navigate to models.py and define the database structure (remember to create Django model classes that inherit from django.db.models.Model.)
NOTE: 
        -- remember to makemigrations and also the migrate commands. This ensures that changes made in the db are captured then also runserver 
        -- also remember to make matching sure that information in the db is similar to that which one wants to show the users

16. These changes of the db are also made in the admin.py file helps one to be able to access the django admin interface
