from django.urls import path
from . import views
import include

app_name = 'pokedex'
urlpatterns = [
    path('home/<int:pokemon_id>/', views.home, name="index"),
]
