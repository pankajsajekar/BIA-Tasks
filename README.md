# BIA-Tasks

## Follow the installation steps

1. Clone the repository:

```bash
git clone https://github.com/jayeshn10/movie-manager-tool/
cd movie-manager-tool
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

```
Download & Install IMAGEMAGICK and the update path "IMAGEMAGICK_BINARY" in settings.py last row
Download Link https://imagemagick.org/script/download.php#windows
```
6. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```
7. Run server
```
python manage.py runserver

```
7. If Your Are using My SQLite Database \n
Login in Djano admin panel using bellow Crediential.
```
Username: Admin
Password: 321

```