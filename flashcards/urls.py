from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deck/<int:deck_id>/', views.deck_detail, name='deck_detail'), 
    path('deck/<int:deck_id>/add/', views.add_flashcard, name='add_flashcard'),
]
