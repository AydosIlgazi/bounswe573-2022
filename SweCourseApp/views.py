from django.http import HttpResponse, HttpResponseRedirect


from .models import LearningSpace, Topic, Prerequisite, Question,Choice
from. forms import LearningSpaceForm, TopicForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
import sys

def index(request):
    learning_space_list =  LearningSpace.objects.all()[:5]          
    context = {'learning_space_list': learning_space_list}
    return render(request, 'SweCourseApp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question = Question.objects.get(pk=question_id)
    return render(request, 'SweCourseApp/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'swecourseapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('swecourseapp:results', args=(question.id,)))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'SweCourseApp/signup.html', {'form': form})

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'SweCourseApp/login.html', {'form': form})

def create_learning_space(request, learning_space_id=None):
    if learning_space_id:
        learning_space = get_object_or_404(LearningSpace, pk=learning_space_id)
    else:
        learning_space = LearningSpace(creator = request.user)
    form = LearningSpaceForm(request.POST or None, instance=learning_space)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'SweCourseApp/createlearningspace.html', {'form': form})

def learning_space(request, learning_space_id):
    learning_space = get_object_or_404(LearningSpace, pk=learning_space_id)
    context = {'learning_space': learning_space}
    return render(request, 'SweCourseApp/learningspace.html', context)

def create_topic(request, learning_space_id,topic_id=None):

    all_topics = Topic.objects.filter(learning_space_id=learning_space_id).exclude(pk = topic_id)
    current_prerequisites= Prerequisite.objects.filter(main_topic=topic_id)
    prerequisiteform =[]
    for existing_topic in all_topics.iterator():
        if(current_prerequisites.filter(prerequisite_topic = existing_topic.id)):
            prerequisiteform.append(
            {
                'id':existing_topic.id,
                'value':1,
                'name': existing_topic.title
            })
        else:
            prerequisiteform.append(
            {
                'id':existing_topic.id,
                'value':0,
                'name': existing_topic.title
            })
    if topic_id:
        topic = get_object_or_404(Topic, pk=topic_id)
    else:
        topic = Topic(learning_space_id = learning_space_id)
    form = TopicForm(request.POST or None, instance=topic)
    if request.method == "POST":
        if form.is_valid():
            prerequisites = request.POST.getlist('prerequisite')
            new_topic=form.save()
            Prerequisite.objects.filter(main_topic=topic_id).delete()
            for pre in prerequisites:
                pre_topic = Topic.objects.get(pk=pre)
                Prerequisite.objects.create(main_topic=new_topic,prerequisite_topic=pre_topic)
            return HttpResponseRedirect('/')
    return render(request, 'SweCourseApp/createtopic.html', {'form': form, 'prerequisiteform':prerequisiteform})

