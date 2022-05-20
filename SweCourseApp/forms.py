from django import forms
from .models import LearningSpace,Topic, Resource, Comment, Notes

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_date','resource','user']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ['topic','user']