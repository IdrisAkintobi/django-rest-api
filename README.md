# Django REST API

This is a simple Django REST API with user authentication and a blog.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running:

1. **Clone the repo:**
   ```
   git clone https://github.com/IdrisAkintobi/django-rest-api.git
   ```
2. **Create a virtual environment:**
   ```
   python -m venv .venv
   ```
3. **Activate the virtual environment:**
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```
4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
5. **Apply migrations:**
   ```
   python manage.py migrate
   ```
6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Running the tests

Explain how to run the automated tests for this system:

```
python manage.py test
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs

## Authors

* **Idris Akintobi** - *Initial work* - [IdrisAkintobi](https://github.com/IdrisAkintobi)

