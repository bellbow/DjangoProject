from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all())
    class Meta:
        model = Comment
        fields = ['comment', 'pizza']
