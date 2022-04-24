from django import forms
from .models import LearningSpace

class LearningSpaceForm(forms.ModelForm):
    
    class Meta:
        model = LearningSpace
        exclude = ['creator']


