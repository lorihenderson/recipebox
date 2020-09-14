"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes.views import index, author_detail, recipe_detail, add_author, add_recipe, login_view, logout_view, favorite_view, edit_view

urlpatterns = [
    path('', index, name='homepage'),
    path('recipe/<int:recipe_id>/edit/', edit_view),
    path('recipe/<int:recipe_id>/', recipe_detail),
    path('author/<int:author_id>/', author_detail),
    path('addauthor/', add_author),
    path('addrecipe/', add_recipe),
    path('login/', login_view),
    path('logout/', logout_view),
    path('favorite/<int:favorite_id>/', favorite_view),
    # path('signup/', signup_view),
    path('admin/', admin.site.urls),
]
