from django import forms
from recipes.models import Author, Recipe


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=120)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
