'''
type of methods 
get 
post
delete 
put 
patch


MVT 

MODEL VIEW    TEMPLATE 
DB     LOGIC     HTML


why learn django 
it a batteries included framework - meaning it comes with a lot of functionalities outside the box
simple syntax (python)
orm object relational mapper so there is no need to write raw sql 
it comes with an admin interface
handles security
user authentication - it can be setup easily and can be extended to be more robust

django templates 

variables {{blog_title}}
tags {% if has_title %}
filters {{ blog_title|title }}

for production we install gunicorn that runs it
and whitenoise a package to help django read static files

use render to host django app 

now  we create a build.sh in project directory
and instead of the build command of pip install -r requirements.txt 
do ./build.sh



# instead of using sql commands we use a model manager in django called objects to perform crud operations
''' 