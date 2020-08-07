from django.shortcuts import render
from recipes.models import Author, Recipes

def index(request):
    my_recipes = Recipes.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "recipebox": "Welcome to Recipebox"})

def author_detail(request, author_id):
    my_recipe = Recipes.objects.filter(author=author_id)
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": my_author, "author_recipes": my_recipe})

def recipe_detail(request, recipe_id):
    my_recipe = Recipes.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipes": my_recipe})

