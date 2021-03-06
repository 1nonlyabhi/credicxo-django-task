<h1 align='center'>
  Hi there 👋 I'm Abhishek 👨‍💻
</h1>

<p align='center'>
  This is the Django Task submitted by me for Credicxo Django Developer Role.
</p>



<p align='center'>

  <a href="https://www.linkedin.com/in/1nonlyabhi/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://twitter.com/1nonlyabhi">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />        
  </a>&nbsp;&nbsp;

</p>


## Setup

1. Git Clone the project with: ```git clone https://github.com/1nonlyabhi/credicxo-django-task```.

2. Move to the base directory: ```cd credicxo-django-task```

3. Create a new python enveronment with: ```python -m venv credicxo-env```.

4. Activate enveronment with: ```credicxo-env\Scripts\activate``` on windows, or ```source credicxo-env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.

8. Download postman from: ```https://www.postman.com/downloads/```.


## Task: 
Create `REST APIs` based on Django with `PostgreSQL` database. It should contain:
1. User Sign Up/Forgot Password APIs.
2. Uses JWT authentication.
3. Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Use internal Django Groups to achieve the same).
4. Teacher must be able to add/list the students.
5. Admin must be able to add/list every user in the database.
6. Students must be able to see his information only.
7. Code should be commented for clarity.


## Requests

#### Register the user

`POST /users/register`

    {
        "username": "username",
        "email": "emailaddress@gmail.com",
        "password": "password"
    }

#### Generate the access token

`POST /api/token/`

    {
        "username": "username",
        "email": "emailaddress@gmail.com",
    }


#### To reset password

`POST /api/password_reset/`

    {
        "email": "emailaddress@gmail.com"
    }

* _It'll print a token in Backend Terminal Console._

#### To confirm reset password

`POST /api/password_reset/`

    {
        "token":"<token>",
        "password":"Password@123"
    }


#### To add the new user to the database

`POST /users/manage`

    {
        "username": "studentnew",
        "email": "studentnew@gmail.com",
        "password": "studentnew",
        "groups": [3]
    }

* _Student (Group no 3) is unable to add anyone to the database._
* _Teacher (Group no 2) is able to add Students to the database._
* _Super-admin (Group no 1) is able to add anyone to the database._


#### To list users from the database

* `GET /users/manage`

* _Student (Group no 3) is able to list his information from the database._
* _Teacher (Group no 2) is able to list Students' information from the database._
* _Super-admin (Group no 1) is able to list anyone's information from the database._
