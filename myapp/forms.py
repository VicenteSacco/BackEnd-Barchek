from django import forms
from .models import Alcohol

class AlcoholForm(forms.ModelForm):
    class Meta:
        model = Alcohol
        fields = '__all__'
