from django.contrib import admin
from django.urls import path, include
from flashcards import views  # for signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flashcards.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 🔐 login/logout
    path('signup/', views.signup, name='signup'),            # 🔐 signup
]