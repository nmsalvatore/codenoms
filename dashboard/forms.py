from django.forms import ModelForm
from django import forms
from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        labels = {'title': ''}
        widgets = {'title': forms.TextInput(attrs={"placeholder": "Title"})}
