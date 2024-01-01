# BIA-Tasks

## Basic Detials
For Each Tasks having seprate Django application (task1, task2, task3 ... ) 
1. Task1 - Framework Setup & Render the string
2. Task2 - Django REST framework API for managing a collection book
3. Task3 - Post a new content to Interacting with database
4. Task4 - Authentication With JWT Token
5. Task5 - Video Generation using MoviePY used API

i recommend you test Task5 From Postman 
<br>You can used Swagger for checking URL Endpoint just uncomment the Swagger line in BIA project urls.py file

## Follow the installation steps

1. Clone the repository:

```bash
git clone https://github.com/pankajsajekar/BIA-Tasks.git
cd BIA-Tasks
```
2. Create a virtual environment
```
python -m venv venv

```
3. Activate virtual environment
```
command - .\venv\Scripts\activate
```
4. Install packages from requirements file
```
pip install -r requirements.txt
```
5. Required IMAGEMAGICK Application in Video Generation Task

Download Link https://imagemagick.org/script/download.php#windows
```
Download & Install IMAGEMAGICK and the update path "IMAGEMAGICK_BINARY" in settings.py last row
```

6. Create Database
```
python manage.py makemigrations
python manage.py migrate
```
7. Run server
```
python manage.py runserver
```
8. If Your Are using My SQLite Database
Login in Djano admin panel using bellow Crediential.
```
Username: Admin
Password: 321
```


##### Additional : I Added Postman Collection json file just import and used them.
