from django.shortcuts import render
from .models import Deck

def home(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/home.html', {'decks': decks})

from django.shortcuts import render, get_object_or_404
from .models import Deck

def deck_detail(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    flashcards = deck.flashcards.all()  
    return render(request, 'flashcards/deck_detail.html', {
        'deck': deck,
        'flashcards': flashcards
    })

from django.shortcuts import render, redirect
from .models import Deck, Flashcard

def add_flashcard(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    
    if request.method == 'POST':
        front = request.POST.get('front')
        back = request.POST.get('back')
        if front and back:
            Flashcard.objects.create(deck=deck, front=front, back=back)
            return redirect('deck_detail', deck_id=deck.id)
    
    return render(request, 'flashcards/add_flashcard.html', {'deck': deck})