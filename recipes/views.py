from django.shortcuts import render, HttpResponseRedirect, reverse
from recipes.models import Author, Recipe
from recipes.forms import AddRecipeForm, AddAuthorForm


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "recipebox": "Welcome to Recipebox"})


def author_detail(request, author_id):
    my_recipe = Recipe.objects.filter(author=author_id)
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": my_author, "author_recipes": my_recipe})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipes": my_recipe})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get("title"),
                time_required = data.get("time_required"),
                description = data.get("description"),
                instructions = data.get("instructions"),
                author = data.get("author"),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"form": form})


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})