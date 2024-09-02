## Django Pokedex Application

# Overview

This Django application provides a Pokedex system that allows users to manage Pokémon data. It includes functionalities to create, read, and update Pokémon records, along with their associated moves, types, and sprites.

Features

- Pokémon Management: Create, view, and update Pokémon records.
- API Integration: Fetch Pokémon data from external APIs and save it to the database.

# Requirements

- Python 3.x
- Django 3.x or higher
- PostgreSQL (or any other database supported by Django)

# Installation

1. Clone the repository:

   git clone https://github.com/wilderherrera/u_andes_pokedex_test.git

3. Navigate to the project directory:

   cd u_andes_pokedex_test

4. Create and activate a virtual environment:

   python3 -m venv env
   source env/bin/activate

5. Install the required dependencies:

   pip install -r requirements.txt

6. Set up the database:

   - Ensure PostgreSQL is installed and running.
   - Create a PostgreSQL database:

     createdb pokedex_db

   - Update `settings.py` with your database credentials:

     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'pokedex_db',
             'USER': 'yourusername',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }

7. Apply migrations:

   python manage.py makemigrations
   python manage.py migrate

8. Create a superuser (optional, for admin access):

   python manage.py createsuperuser

9. Run the development server:

   python manage.py runserver

   The application should now be accessible at http://127.0.0.1:8000/.

# Swagger
  
   You could get api information 

http://localhost:8000/swagger/

![image](https://github.com/user-attachments/assets/d917c96d-04ec-407e-96a3-e6eddd3b1563)

 
# Testing
   Run unit test:
    
   **python manage.py test**

# Usage

- Admin Interface: Access the Django admin interface at http://127.0.0.1:8000/admin/ to manage Pokémon, moves, types, and sprites.
- API Endpoints: Interact with the API endpoints to create, update and retrieve Pokémon data.

# File Structure

# File Structure

- pokedex/: Contains the core Django app with models, views, serializers, and URLs.
- pokedex/common/: Contains common utilities to use throughout the project.
- pokedex/middleware/: Contains project-specific middleware.
- pokedex/migrations/: Contains database migration files.
- pokedex/models/: Contains Django models that define the structure of the database.
- pokedex/repositories/: Contains repository classes that handle the interaction with the database, such as querying and persisting data (e.g., pokemon_repository.py).
- pokedex/serializers/: Contains serializers used to transform complex data types such as querysets and model instances into native Python data types for JSON rendering.
- pokedex/serializers/models/: Contains model serializers specific to Pokémon and related entities (e.g., pokedex_pokemon_serializer.py, pokemon_list_serializer.py).
- pokedex/services/: Contains service classes that encapsulate the business logic of the application (e.g., poke_api_service.py, pokemon_service.py).
- pokedex/views/: Contains view classes that handle the HTTP requests and return the appropriate responses.
- pokedex/views/v1/: Contains version 1 of the API views, organizing the app’s endpoints.


# Middleware

This application includes custom middleware that interacts with external APIs to fetch and update Pokémon data.

# Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

# License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
