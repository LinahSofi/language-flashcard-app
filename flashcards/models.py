# flashcards/models.py

from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')
    front = models.CharField(max_length=255)
    back = models.TextField()

    def __str__(self):
        return self.front