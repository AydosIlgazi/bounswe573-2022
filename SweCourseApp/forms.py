from django import forms
from .models import LearningSpace,Topic, Resource

class LearningSpaceForm(forms.ModelForm):
    
    class Meta:
        model = LearningSpace
        exclude = ['creator']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ['learning_space']
    
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        exclude = ['likes','dislikes','created_date','topic','user']