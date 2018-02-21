from django import forms
from bootstrap_datepicker.widgets import DatePicker
from .models import Excercise

class ExcerciseForm(forms.ModelForm):

    class Meta:
        model = Excercise
        fields = ('group', 'title', 'text',)

class ToDoForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )