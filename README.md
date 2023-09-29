Django-based cryptocurrency exchange platform

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- Docker (if you want to run the project in a container)

### Installing Dependencies

1. Clone the repository to your local machine:

    ➜ ~ git clone git@github.com:saharmirjavadi/exchange.git
   

2. Change into the project directory:

    ➜ ~ cd exchange


3. Create a virtual environment (recommended) and activate it:
    
    ➜ ~ python -m venv venv
    ➜ ~ source venv/bin/activate


4. Install the project dependencies using pip:

    ➜ ~ pip install -r requirements.txt


### Configuration

1. Create a .env file in the project's root directory and configure your environment variables like DB_NAME, DB_USER, DB_PASSWORD, etc.(you can copy .env.example)

2. Configure your database settings in settings.py. Make sure it matches your .env file.


### Database Setup

* If you have Docker installed, you can easily set up a PostgreSQL database container:

    ➜ ~ docker compose build
    ➜ ~ docker compose up -d


* Creating a Database and Database User in postgres:

- Log into an interactive Postgres session by typing:

    ➜ ~ sudo -u postgres psql

- First, you will create a database for the Django project.

    postgres=# CREATE DATABASE db_name;

- Next, you will create a database user which you will use to connect to and interact with the database.

    postgres=# CREATE USER 'username' WITH PASSWORD 'password';

- Now, all you need to do is give your database user access rights to the database you created:

    postgres=# GRANT ALL PRIVILEGES ON DATABASE db_name TO username;

- Exit the SQL prompt to get back to the postgres user’s shell session:

    postgres=# \q


* Apply the database migrations:

    ➜ ~ python manage.py makemigrations
    ➜ ~ python manage.py migrate


### Running the Development Server

Start the Django development server:

    ➜ ~ python manage.py runserver


### Running Tests
You can run the project's tests using:

    ➜ ~ python manage.py test


### Running App
Finally to Run this project:

    http://server_domain_or_IP:8000
    

### API Documentation (Swagger)

    You can access the API documentation at http://server_domain_or_IP:8000/swagger/ after logging in with the admin credentials.