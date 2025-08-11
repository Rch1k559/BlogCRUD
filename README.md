# BlogCRUD
A simple Django web application for creating, editing, and deleting blog posts.   Includes basic CRUD functionality, user-friendly interface, and database integration.

## Functionality
- Create new blog posts
- Edit existing posts
- Delete posts
- View list of posts
- Simple and clear code structure

## Technologies
- Python 3.x
- Django 5.x
- SQLite (default)
- HTML, CSS

## Installation and Startup

1. **Clone repository**
bash
git clone https://github.com/username/blogcrud.git
cd blogcrud

Create and activate virtual environment
python -m venv venv
# For macOS/Linux
source venv/bin/activate
# For Windows
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makemigrations
python manage.py migrate

Start server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

License
This project is created for educational purposes. You can use and modify it freely.
