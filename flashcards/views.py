import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages  # ✅ Add this
from .models import Deck, Flashcard

# Home Page — View All Decks
def home(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/home.html', {'decks': decks})

# Deck Detail — Show All Flashcards in a Deck
def deck_detail(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    flashcards = deck.flashcards.all()  
    return render(request, 'flashcards/deck_detail.html', {
        'deck': deck,
        'flashcards': flashcards
    })

# Flashcard CRUD
def add_flashcard(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        front = request.POST.get('front')
        back = request.POST.get('back')
        if front and back:
            Flashcard.objects.create(deck=deck, front=front, back=back)
            messages.success(request, 'Flashcard added successfully.')
            return redirect('deck_detail', deck_id=deck.id)
        else:
            messages.error(request, 'Both front and back are required.')
    return render(request, 'flashcards/add_flashcard.html', {'deck': deck})

def edit_flashcard(request, deck_id, card_id):
    deck = get_object_or_404(Deck, id=deck_id)
    flashcard = get_object_or_404(Flashcard, id=card_id, deck=deck)
    if request.method == 'POST':
        flashcard.front = request.POST.get('front')
        flashcard.back = request.POST.get('back')
        flashcard.save()
        messages.success(request, 'Flashcard updated.')
        return redirect('deck_detail', deck_id=deck.id)
    return render(request, 'flashcards/edit_flashcard.html', {
        'deck': deck,
        'flashcard': flashcard
    })

def delete_flashcard(request, deck_id, card_id):
    deck = get_object_or_404(Deck, id=deck_id)
    flashcard = get_object_or_404(Flashcard, id=card_id, deck=deck)
    if request.method == 'POST':
        flashcard.delete()
        messages.success(request, 'Flashcard deleted.')
        return redirect('deck_detail', deck_id=deck.id)
    return render(request, 'flashcards/delete_flashcard.html', {
        'deck': deck,
        'flashcard': flashcard
    })

# Deck CRUD
@require_http_methods(["GET", "POST"])
def add_deck(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Deck.objects.create(name=name)
            messages.success(request, 'Deck created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Deck name cannot be empty.')
    return render(request, 'flashcards/add_deck.html')

def edit_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            deck.name = new_name
            deck.save()
            messages.success(request, 'Deck name updated.')
            return redirect('home')
        else:
            messages.error(request, 'New name cannot be empty.')
    return render(request, 'flashcards/edit_deck.html', {'deck': deck})

def delete_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        deck.delete()
        messages.success(request, 'Deck deleted.')
        return redirect('home')
    return render(request, 'flashcards/delete_deck.html', {'deck': deck})

# Flashcard Review Mode with Known/Review Tracking
@require_http_methods(["GET", "POST"])
@csrf_exempt
def review_flashcards(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            request.session['review_stats'] = data
            request.session.modified = True
            return JsonResponse({'status': 'saved'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid data'}, status=400)

    flashcards = deck.flashcards.all()
    flashcard_data = list(flashcards.values('front', 'back'))
    return render(request, 'flashcards/review_flashcards.html', {
        'deck': deck,
        'flashcards': flashcard_data
    })

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})