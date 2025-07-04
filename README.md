# Language Flashcard App

A Django-based app that helps users create flashcards to study any language.

## Features

- ✅ User Authentication (Signup / Login / Logout)
- ✅ Deck CRUD (Create, View, Edit, Delete)
- ✅ Flashcard CRUD (Add, Edit, Delete)
- ✅ Review Mode with Flip UI (HTML/CSS/JS)
- ✅ Track “I Knew This” vs “Needs Review”
- ✅ Session-based performance tracking
- ✅ Chart.js progress chart
- ✅ Bootstrap 5 Styling
- ✅ Navbar, breadcrumbs, and flash messages
- ✅ User-linked decks (each user sees only their own)
- ✅ Fully configured for deployment

## Tech Stack

- Python 3.8+
- Django 4.2
- SQLite (local dev)
- Bootstrap 5
- JavaScript
- Chart.js

## 🧪 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/LinahSofi/language-flashcard-app.git
cd language-flashcard-app

# Set up virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
touch .env

SECRET_KEY=your-django-secret
DEBUG=False

# Apply migrations and collect static files
python manage.py migrate
python manage.py collectstatic

# Start the server
python manage.py runserver

Environment Variables
	•	SECRET_KEY: Your Django secret key
	•	DEBUG: Should be False in production

Deployment
	•	Uses a Procfile and .env file for deployment to Render.com
	•	STATIC_ROOT is configured for collectstatic
	•	python-decouple used to hide secrets

User Stories
	1.	As a language learner, I want to create decks for different topics or languages.
	2.	As a user, I want to flip flashcards to test myself and track what I know.
	3.	As a user, I want to log in to save my decks and review progress securely.

📸 Screenshots
Added later 

👩🏻‍💻 Author
Linah Sofi

