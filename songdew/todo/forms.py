from django import forms

from . import models


class TodoForm(forms.ModelForm):
    class Meta:
        fields = ["title", "details", "is_priority"]
        model = models.Todo
