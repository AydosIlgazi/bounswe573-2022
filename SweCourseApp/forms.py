from django import forms
from .models import LearningSpace,Topic

class LearningSpaceForm(forms.ModelForm):
    
    class Meta:
        model = LearningSpace
        exclude = ['creator']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ['learning_space']