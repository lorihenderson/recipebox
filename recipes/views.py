from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from recipes.models import Author, Recipe
from recipes.forms import AddRecipeForm, AddAuthorForm, LoginForm


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


@login_required
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
                author = request.user.author,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"form": form})


@login_required
@staff_member_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(
                name = data.get("name"),
                bio = data.get("bio"),
                user = new_user,
            )
            return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "add_author.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def favorite_view(request, favorite_id):
    logged_in_user = request.user
    fav_recipe = Recipe.objects.filter(id=favorite_id).first()
    logged_in_user.author.favorites.add(fav_recipe)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def edit_view(request, recipe_id):
      recipe_initial = Recipe.objects.filter(id=recipe_id).first()
      recipe_dict = {"title": recipe_initial.title, "time_required": recipe_initial.time_required, "description": recipe_initial.description, "instructions": recipe_initial.instructions}
      if request.user.is_staff or request.user.author == recipe_initial.author:
        form = AddRecipeForm(initial=recipe_dict)
        if request.method == "POST":
              form = AddRecipeForm(request.POST, initial=recipe_dict)
              if form.is_valid():
                data = form.cleaned_data
                recipe_initial.title = data.get("title")
                recipe_initial.time_required = data.get("time_required")
                recipe_initial.description = data.get("description")
                recipe_initial.instructions = data.get("instructions")

                recipe_initial.save()
                return HttpResponseRedirect(reverse("homepage"))
        return render(request, "add_recipe.html", {"form": form})
      else:
        return HttpResponse("Access Denied")