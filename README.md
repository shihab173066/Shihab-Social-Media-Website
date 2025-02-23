User Credentials for Testing:

Test User 1
Auni
123

Test User 2
Md
123

Note: Make as much users as you want to

Setup and Installation Instructions:

Clone the repository:
git clone https://github.com/shihab173066/Shihab-Social-Media-Website.git

Navigate to the project directory:
cd socialmedia

Create a virtual environment (recommended):
virtualenv venv

Activate the virtual environment:
venv\Scripts\activate

Install the project dependencies:
pip install pillow

Perform database migrations:
python manage.py migrate

Superadmin User -
Username: shihab
Email address: shihab@email.com
Password: 123

python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/