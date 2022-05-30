# CoLearning

A colearning application where users can share his knowledge and learn with other users.

## Description

A web application which provides learning environment to users. Users can create spaces and topics to subjects they want to learn together. In this spaces, participants can share resources, materials and add comments to resources. Moreover, application enables users to take notes on topics and see other users' notes. Note taking is an important process that is performed during learning activity. 

## Getting Started

### Running Application in Local

#### Dependencies

* Python
* Django
* MySql Database

#### Installing

* Clone this repository
* Install packages in requirements.txt
  * Cd to the directory where requirements.txt is located
  * Activate your virtualenv
  * run: `pip install -r requirements.txt`
* Update this database information according to your db
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}   
```
* Activate virtual environment
* Run following commands to create tables in database
```
python manage.py makemigrations
python manage.py migrate
```

#### Executing program

* Run following command to run application
```
python manage.py runserver
```

### Running Application in Docker

#### Dependencies

* Docker
* MySql

#### Installing

* Database settings declared as environment variables, no modification needed

#### Executing program

* Docker Run
```
docker run -d -e DATABASE_NAME=colearning -e DATABASE_HOST=<your-database-host> -e DATABASE_USER=<your-database-user> -e DATABASE_PASSWORD=<your-database-password> -e DATABASE_PORT=<your-database-port> -p 80:8000 aydosilgazi/django_colearning
```




## Version History

* 0.9
    * Initial Release



## Acknowledgments

Inspiration, code snippets, etc.
* [bootstrap](https://getbootstrap.com/)
* [fontawesome](https://fontawesome.com/)
* [jquery](https://jquery.com/)
* [flaticon](https://www.flaticon.com/)
