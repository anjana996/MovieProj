from django import forms
from .models import Category, MovieDetails

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieDetails
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

