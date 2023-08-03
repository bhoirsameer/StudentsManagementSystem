Follow the steps tom run project
step 1:
    run this commands on terminal--->
    Py manage.py makemigrations
    Py manage.py migrate


Step 2:
    run a command on terminal--->Py manage.py createsuperuser


Step 3:
    run a command on terminal--->Py manage.py runserver
    now add (admin) in url in browser
    login using username and password (superuser username and password) 


Step 4:
    After login click on add link in host and create new username and password
    This username and password are for admin login 
    Click on trainers here we have to create username an passwords for each department ---> Note I kept this usernames fix
    so add below details as it is
    a : username=IT              password=123
    b : username=Mechanical      password=123
    c : username=Civil           password=123


Step 5:
    Run a command on terminal--->Py manage.py runserver
    now click on admin link give username and passwords
    after login in manage courses ther are 3 departments IT ,
    Mech , Civil at at least 3 courses in each department


step 6:
    Now add the trainers for each department and click on home


Step 7:
    trainers can login by the username and passord given at 4th step
    
