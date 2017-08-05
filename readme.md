# environment setup
## a virtual environment is created within this folder, use virtualenv to create the virtual environments
virtual environment needs to be activated by using
'source PROJECT/bin/activate'
if done using the virtual environment, use 'deactivate' to deactivate it.
**make sure to activate the envirnment before run it**

# Django installation and set up
## Django -1.11 is installed
use 'django-admin startproject PROJECT' to create a project.
a project named **entry** was created.

# Deploy the server
-go to the PROJECT folder,use 'python manage.py runserver' to start the server(default listening at port 8000)
-use 'python manage.py runserver PORTNUMBER' to specify the port.
-us 'python manage.py runserver IP:PORTNUMBER' to specify both server's IP address and portnumber.
-go to httpd apahce configue file and modify the proxypass to listen to prot 8001

## This project's full path is 'JS_django/Entry'
## The actual configuration and setting is located at 'JS_django/Entry/Entry'
## The file 
