# MyPaymentsDataAnalysis
A payment gateway data analysis app that shows the different statistics of different installed apps that uses the payment sdks. Django Rest is used for backend api and React is used for the UI.
# Installation
- Clone this repository via `git clone https://github.com/parvez86/MyPaymentsDataAnalysis.git`
- <b>Backend<b>:
  - Requires the following packages:
    - Python 3.9.7 or higher
    - Django 4.0 or higher

  It is recommended to use virtual environment packages such as virtualenv. Follow the steps below to setup the project:
    - Use this command to install required packages `pip install -r requirements.txt`
    - Check Migrations of the project via terminal: `python manage.py makemigrations`
    - Migrate the project from terminal: `python manage.py migrate`
    - Create admin user for admin panel from terminal: `python manage.py createsuperuser`. And enter the username, email and password. 
    - Run the project from terminal: `python manage.py runserver`
- <b>Frontend</b>:
  - go to the folder myappp
  - Run command: `npm start`



