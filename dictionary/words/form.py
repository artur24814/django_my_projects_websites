from django import forms
from .models import Words

class WordsForm(forms.ModelForm):
    """
    form for creating word for dictionary
    """
    class Meta:
        model = Words
        fields = [
            'word',
            'definition',
        ]