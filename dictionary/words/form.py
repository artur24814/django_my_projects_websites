from django import forms
from .models import Words

class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = [
            'word',
            'definition',
        ]