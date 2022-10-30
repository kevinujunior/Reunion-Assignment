# Reuinion Assignment

## Tests
- Functional Test cases are in "Test Cases.xlsx"
- There are total of 13 test cases written in two files
- These test files in user/tests.py and post/tests.py

**Write Following Command in terminal to use test files**
>```python manage.py test```

### Google Drive Link to Docker Image is in "docker_image.txt"

### Running Server
> ```python manage.py runserver```

### Creating SuperUser
> ```python manage.py createsuperuser```

**Once your server starts running try testing the APIs**
**Cheers**

## Working with Docker

To generate docker image from Dockerfile
> ```docker build -t reuinion .```

To load prebuilt docker image
> ```docker load -i <image_name>.tar```

Running the image in container
> ```docker run -d -p 8000:8000 <image_name>```

### [Heroku Link](https://kevin-reunion-assignment.herokuapp.com/)