
from django.test import TestCase, Client,  RequestFactory
from matplotlib.pyplot import title 
from SweCourseApp.models import LearningSpace, Topic
from django.contrib.auth.models import User
from django.urls import reverse

from SweCourseApp.views import learning_space


class SignUpViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/signup/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('swecourseapp:signup'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('swecourseapp:signup'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/signup.html')

class LoginViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		
		
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/login/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('swecourseapp:login'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('swecourseapp:login'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/login.html')

class LearningSpaceViewTest(TestCase):
	@classmethod
	def setUpTestData(self):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=test_user)
		
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/learningspace/' + str(self.learning_space.id))
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('swecourseapp:learningspace', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('swecourseapp:learningspace', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/learningspace.html')

class RoadMapViewTest(TestCase):
	@classmethod
	def setUpTestData(self):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=test_user)
		
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/learningspace/' + str(self.learning_space.id) + '/roadmap')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('swecourseapp:roadmap', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('swecourseapp:roadmap', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/roadmap.html')

class TopicViewTest(TestCase):
	@classmethod
	def setUpTestData(self):
		self.test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=self.test_user)
		self.topic = Topic.objects.create(title = 'Test Toic Title', content='Test Content', learning_space=self.learning_space)
		
	def test_view_url_exists_at_desired_location(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		response = self.client.get('/learningspace/' + str(self.learning_space.id) + '/topic/'+ str(self.topic.id))
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		response = self.client.get(reverse('swecourseapp:topic', kwargs={'learning_space_id':self.learning_space.id, 'topic_id':self.topic.id}))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		response = self.client.get(reverse('swecourseapp:topic', kwargs={'learning_space_id':self.learning_space.id, 'topic_id':self.topic.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/topic.html')

	def test_view_not_visible_without_login(self):
		response = self.client.get(reverse('swecourseapp:topic', kwargs={'learning_space_id':self.learning_space.id, 'topic_id':self.topic.id}))
		self.assertEqual(response.status_code, 302)

class TopicsViewTest(TestCase):
	@classmethod
	def setUpTestData(self):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=test_user)
		
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/learningspace/' + str(self.learning_space.id) + '/topics')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('swecourseapp:topics', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('swecourseapp:topics', kwargs={'learning_space_id':self.learning_space.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'SweCourseApp/topics.html')

class CreateLearningSpaceTest(TestCase):
	@classmethod
	def setUpTestData(self):
		self.test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.client = Client()
	
	def test_view_learningspace_created_successfully(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		response =self.client.post(reverse('swecourseapp:createlearningspace'), {'title':'test title', 'description':'test description'})
		created_space = LearningSpace.objects.last()
		self.assertRedirects(response, reverse('swecourseapp:learningspace', kwargs={'learning_space_id':created_space.id}), fetch_redirect_response=False)
	
	def test_view_learningspace_not_created_wrong_data(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		response =self.client.post(reverse('swecourseapp:createlearningspace'), {'description':'test description'})
		self.assertFormError(response, 'form', 'title', 'This field is required.')

	def test_view_learningspace_not_created_without_login(self):
		response =self.client.post(reverse('swecourseapp:createlearningspace'), {'title':'test title', 'description':'test description'})
		self.assertRedirects(response, '/login/?next=/createlearningspace/', fetch_redirect_response=False)

class CreateTopicTest(TestCase):
	@classmethod
	def setUpTestData(self):
		self.test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		self.learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=self.test_user)
		self.client = Client()
	
	def test_view_topic_created_successfully(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		url = '/learningspace/' + str(self.learning_space.id) + '/createtopic'
		response =self.client.post(url, {'title':'test title', 'content':'test content'})
		self.assertRedirects(response, reverse('swecourseapp:topics', kwargs={'learning_space_id':self.learning_space.id}), fetch_redirect_response=False)

	def test_view_topic_not_created_wrong_data(self):
		self.client.login(username= self.test_user.username, password = '1X<ISRUkw+tuK')
		url = '/learningspace/' + str(self.learning_space.id) + '/createtopic'
		response =self.client.post(url, { 'content':'test content'})
		self.assertFormError(response, 'form', 'title', 'This field is required.')

	def test_view_topic_not_created_without_login(self):
		url = '/learningspace/' + str(self.learning_space.id) + '/createtopic'
		response =self.client.post(url, {'title':'test title', 'content':'test content'})
		self.assertRedirects(response, '/login/?next=/learningspace/4/createtopic', fetch_redirect_response=False)
	





