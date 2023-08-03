# User Onboarding

API is build using Django Rest Framework (DRF)
<br>
Database used for this project: MySQL

### Requirements
```
asgiref==3.7.2
Django==4.2.4
djangorestframework==3.14.0
Markdown==3.4.4
mysqlclient==2.2.0
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3
```
To install all the files, use this command `pip install -r requirements.txt`

### Routes
```
SignUp: http://127.0.0.1:8000/signup
LogIn: http://127.0.0.1:8000/login
```

### Test
use `test.rest` file or use `thunder` or `postman` for testing <br>
`test.rest` file look like this
```rest
POST http://127.0.0.1:8000/login
Content-Type: application/json

{"username":"test","password":"pass123"}

###

POST http://127.0.0.1:8000/signup
Content-Type: application/json

{"username":"test1","password":"test1pass","email":"test1@gmail.com"}
```



