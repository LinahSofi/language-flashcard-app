# Language Flashcard App

A Django-based web app for creating and reviewing language flashcards. Users can create decks, add flashcards, and later track their learning progress. This app is built as a capstone project for the Full-Stack Engineering Bootcamp at Cal State University.

> **Work In Progress** — Core features are in place. More functionality (review mode, charts, auth) coming soon.

---

## User Story

1.	As a language learner,
I want to create flashcard decks for different topics or languages,
So that I can organize my vocabulary by category.
2.	As a student,
I want to add new flashcards with a front (question/word) and back (answer/translation),
So that I can actively review and memorize information.
3.	As a daily learner,
I want to view and manage all my flashcards in one place,
So that I can build consistent study habits and track my progress.

Future enhancements will allow:
- Tracking review history and progress
- Logging in to access personal decks
- Practicing cards via flip animations

---

## Project Structure
language-flashcard-app/
├── flashcard_project/       # Django project config
├── flashcards/              # Flashcards app (models, views, templates)
│   ├── templates/
│   │   └── flashcards/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── deck_detail.html
│   │       └── add_flashcard.html
├── db.sqlite3               # Local SQLite database
├── manage.py
└── README.md

---

## Features Implemented (Day 1)

- [x] Project planning (user stories, wireframes)
- [x] Django project + app setup
- [x] Models: `Deck` and `Flashcard`
- [x] Admin panel enabled
- [x] View decks and flashcards
- [x] Add flashcard via form
- [x] Basic styling with Bootstrap
- [x] GitHub repo created and pushed ✅

---

## Upcoming Features

- [ ] Flashcard review/flip mode
- [ ] Edit/delete flashcards
- [ ] User login and personalization
- [ ] Charted learning progress
- [ ] Responsive UI enhancements

---

## Screenshots

*(To be added in later updates)*

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/LinahSofi/language-flashcard-app.git
   cd language-flashcard-app

## Credits

Created by Linah Sofi
Capstone Project — Full-Stack Engineering Bootcamp, Cal State University

## Timeline

June 27
Planning, models, views
Done

June 27
GitHub repo + README setup
Done

June 28+
CRUD, UI, auth, charts
In Progress

