# Employeum

Employeum is a Django-based web application for companies to create a profile and employees to create individual profiles and showcase their portfolios and projects. The application is designed to help companies connect with potential employees more efficiently and effectively.

## Features

* Company and employee registration and login
* Profile creation and editing for both companies and employees
* Portfolio and project creation and editing for employees
* Search and filter functionality for companies
* Responsive design for mobile and desktop devices

## Installation

To install Employeum, follow these steps:

1. Clone this repository: 
    ```bash
    git clone https://github.com/shaheem-pp/employeum_django
    ```
2. Create a virtual environment and activate it: 
    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```
3. Install the dependencies: 
    ```bash
    pip install -r requirements.txt
    ```
4. In python terminal generate secretkey and paste it with variable `SECRET_KEY` in .env file inside project directory(directory with settings.py)
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
5. Migrate the database: 
    ```bash
    python manage.py migrate
    ```
6. Create a superuser: 
    ```bash
    python manage.py createsuperuser
    ```
7. Start the development server: 
    ```bash
    python manage.py runserver
    ```

The application will be available at http://localhost:8000/.

## Contributing

If you would like to contribute to Employeum, please follow these guidelines:

1. Fork this repository
2. Create a branch for your feature: 
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them: 
    ```bash
    git commit -m 'Add new feature'
    ```
4. Push your changes to your fork: 
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request

Please make sure your code adheres to PEP8 coding style and includes appropriate tests.

## License

Employeum is released under the MIT License, meaning anyone can use and modify the code, subject to certain conditions. Contributions to the project are welcome, and can include Django, HTML, CSS, JS, jQuery, and design work.

Thank you for considering contributing to the Employeum project!
