🎬 Django Movie Management System

##
This is a beginner-friendly Django project built to revise and strengthen backend development fundamentals.

The project is a simple Movie Management System where users can:

View movies

Add new movies

Delete existing movies

While small, it covers the core workflow of Django — from handling requests to interacting with the database.


🚀 What This Project Demonstrates
##
✔ URL Routing in Django
✔ Creating and using Django Models
✔ Connecting Django with a database
✔ Handling GET and POST requests
✔ Creating views and rendering templates
✔ Performing CRUD operations
✔ Redirecting users after form submission

This project helped me clearly understand the flow:

User Request → URL → View → Database → Template → Response


🛠 Tech Stack
##
Backend: Django (Python)
Frontend: HTML (Django Templates)
Database: SQLite (Default Django DB)


📌 Features
##
🎞 View Movies

Displays all movies stored in the database.

➕ Add Movie

Users can submit a form with movie title and year to add a new movie.

❌ Delete Movie

Allows deleting a movie from the database.


🔄 How It Works (Flow)
##
User visits a URL

Django matches it with a URL pattern

The corresponding view function runs

The view interacts with the Movie model (database)

Data is sent to a template

HTML page is rendered and shown to the user
