🎬 Django Movie Management System

This is a beginner-friendly Django project built to revise and strengthen backend development fundamentals.

The project is a simple Movie Management System where users can view movies, add new movies, and delete existing ones. While small, it covers the core working flow of Django from handling requests to interacting with the database.

🚀 What This Project Demonstrates

✔️ URL Routing in Django
✔️ Creating and using Django Models
✔️ Connecting Django with a database
✔️ Handling GET and POST requests
✔️ Creating views and rendering templates
✔️ Performing CRUD operations
✔️ Redirecting users after form submission

This project helped me clearly understand the flow:

User Request → URL → View → Database → Template → Response

🛠 Tech Stack

Backend: Django (Python)

Frontend: HTML (Django Templates)

Database: SQLite (default Django DB)

📂 Features
🎥 View Movies

Displays all movies stored in the database.

➕ Add Movie

Users can submit a form with movie title and year to add a new movie.

❌ Delete Movie

Allows deleting a movie from the database.

📸 How It Works (Flow)

User visits a URL

Django matches it with a URL pattern

The corresponding view function runs

The view interacts with the Movie model (database)

Data is sent to a template

HTML page is rendered and shown to the user

▶️ How to Run This Project
# Clone the repository
git clone https://github.com/Kulkarnivaishnavi473/django-project.git

# Move into the project folder
cd django-project

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver


Then open your browser and go to:

http://127.0.0.1:8000/movies/

🌱 Why I Built This

I created this project to revise Django fundamentals and strengthen my understanding of backend development concepts like routing, views, models, and templates.

Revisiting the basics helped me gain more confidence in how web frameworks actually work behind the scenes.
