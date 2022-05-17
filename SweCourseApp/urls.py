from django.apps import apps
from django.urls import path

from . import views

app_name = 'swecourseapp'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    path('index/', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    #path('topic/', views.topic, name='topic'),

    path('signup/', views.signup, name='signup'),
    path('login/',views.loginView, name='login'),
    path('createlearningspace/',views.create_learning_space, name='createlearningspace'),
    path('editlearningspace/<int:learning_space_id>', views.create_learning_space, name='editlearningspace'),
    path('learningspace/<int:learning_space_id>',views.learning_space, name='learningspace'),
    path('learningspace/<int:learning_space_id>/createtopic',views.create_topic, name='createtopic' ),
    path('learningspace/<int:learning_space_id>/edittopic/<int:topic_id>',views.create_topic, name='edittopic' ),
    path('learningspace/<int:learning_space_id>/roadmap',views.road_map, name='roadmap'),
    path('learningspace/<int:learning_space_id>/topics',views.topics, name='topics'),
    path('learningspace/<int:learning_space_id>/topic/<int:topic_id>',views.topic, name='topic'),
    path('ajax/postResource', views.postResource, name = 'postresource'),
    path('ajax/likeResource', views.likeResource, name = 'likeResource'),

]