# Simple Django Project for Learning AWS DevOps

This is a simple Django project aimed at helping you learn AWS DevOps practices. It covers the basic setup of a Django project and deployment to Amazon Web Services (AWS) using various DevOps tools and services. 
It serves as the foundation project for working on DevOps projects.


- `smuull/`: Contains project apps
- `config/`: Contains project-level configurations
- `manage.py`: Django's command-line utility for administrative tasks.

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/edward-mike/django-blog-for-devops.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. configurations for environment variables in settings.py
and create a .env file (without extension name) in your project directory
```SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,
DB_NAME=you_db_name
DB_USER=your_db_username
DB_PASSWORD=your_password
DB_HOST=your_hostname
DB_PORT=your_port
PROJECT_NAME=smuull
```

3. Run migrations to create necessary database tables:
```python manage.py migrate
```

4. Start the development server:
```python manage.py runserver
```

Now you should be able to access the project at http://localhost:8000.
## Author

- Author : [Edward Mike](https://www.github.com/octokatherine)
- University : [University of Stirling](https://www.stir.ac.uk/) 

