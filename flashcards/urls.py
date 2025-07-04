from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deck/<int:deck_id>/', views.deck_detail, name='deck_detail'),
    path('deck/<int:deck_id>/add/', views.add_flashcard, name='add_flashcard'),
    path('deck/<int:deck_id>/edit/<int:card_id>/', views.edit_flashcard, name='edit_flashcard'),  # ✅ NEW
    path('deck/<int:deck_id>/delete/<int:card_id>/', views.delete_flashcard, name='delete_flashcard'),  # ✅ NEW
    path('add-deck/', views.add_deck, name='add_deck'), 
        # ✅ Deck CRUD
    path('add-deck/', views.add_deck, name='add_deck'),
    path('edit-deck/<int:deck_id>/', views.edit_deck, name='edit_deck'),         # ✅ NEW
    path('delete-deck/<int:deck_id>/', views.delete_deck, name='delete_deck'),   # ✅ NEW
    path('deck/<int:deck_id>/review/', views.review_flashcards, name='review_flashcards'),
]