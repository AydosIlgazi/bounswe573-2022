from django.http import HttpResponse, HttpResponseRedirect


from .models import LearningSpace, Question,Choice
from. forms import LearningSpaceForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


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

