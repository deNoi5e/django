from django import forms
from .models import Excercise


class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = ('group', 'title', 'text',)
