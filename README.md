# InnoHub
Un étudiant, via la plateforme « InnoHub » peut créer un projet. Les « coachs » consultent les propositions des projets et peuvent valider (ou non) une idée. Un « coach » peut s’inscrire à un ou plusieurs projets. Une idée validée est consultable par les autres étudiants. Ils peuvent ainsi participer à un ou plusieurs autres projets (au Maximum 3). Lorsqu’un étudiant est intéressé par un projet et exprime sa volonté de participation, il doit introduire le nombre de jours qu’il alloue.
# Django_Project
A step by step introduction to Django

1. > pip install virtualenv
2. > virtualenv venv
3. > venv\scripts\activate
4. > pip install django
5. Verify version: 
    > py -m django --version
                       
                       
## Install requirements
requirements.txt contains all the packages you will need for this work.
> pip install -r requirements.txt

# Django Rest Framework
1. > pip install django-rest-framework
2. add to settings.py
> INSTALLED_APPS = [..., 'rest_framework",]
3. add to settings.py

   > REST_FRAMEWORK = {
   
   >   "DEFAULT_PERMISSION_CLASSES":
   
   >      ["rest_framework.permissions.AllowAny", ],
   
   >   "DEFAULT_PARSER_CLASSES": 
   
   >      ["rest_framework.parsers.JSONParser", ],
   
   > }
4. In "RestFramework 4", we change the permession classes:
> ["rest_framework.permissions.AllowAny", ],

becomes

> ["rest_framework.permissions.IsAuthenticated", ],

5. "RestFramework 5": Check api/views.py for changes.

# JSON Web Token Authentication

1. > pip install djangorestframework_simplejwt
2. Add it to the list of authentication classes in settings.py

> REST_FRAMEWORK = { ...
   
   >   "DEFAULT_AUTHENTICATION_CLASSES":  [ 
   
   >      "rest_framework.authentication.SessionAuthentication",
   >      "rest_framework_simplejwt.authentication.JWTAuthentication",
   >    ],
   
   > }
   
 3. Add a serializer for the User (api/serializer.py)
 4. Add a registration view
 5. Check api/urls.py for the new endpoints
 
 
