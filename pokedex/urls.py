from django.urls import path
from . import views
import include

app_name = 'pokedex'
urlpatterns = [
    path('home/<int:pokemon_id>/', views.home, name="index"),
    path('proximo_pokemon/<int:pokemon_id>/', views.proximo_pokemon, name="proximo_pokemon"),
    path('anterior_pokemon/<int:pokemon_id>/', views.anterior_pokemon, name="anterior_pokemon"),
    path('ultimo_pokemon/<int:pokemon_id>/', views.ultimo_pokemon, name="ultimo_pokemon"),

]
