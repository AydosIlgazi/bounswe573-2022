from django.test import TestCase
from SweCourseApp.models import LearningSpace, Topic
from django.contrib.auth.models import User
from django.urls import reverse


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

