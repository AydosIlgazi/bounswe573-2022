from django.test import TestCase
from SweCourseApp.models import LearningSpace, Topic
from django.contrib.auth.models import User


class LearningSpaceModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=test_user)

	def test_object_name_is_title(self):
		learning_space = LearningSpace.objects.get(id=1)
		expected_object_name = 'Test LearningSpace Title'
		self.assertEqual(str(learning_space), expected_object_name)

class TopicModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		learning_space= LearningSpace.objects.create(title='Test LearningSpace Title', description='Test Description', creator=test_user)
		Topic.objects.create(title='Test Topic Title', content='Test Topic Description', learning_space=learning_space)

	def test_object_name_is_title(self):
		topic = Topic.objects.get(id=1)
		expected_object_name = 'Test Topic Title'
		self.assertEqual(str(topic), expected_object_name)

	def test_first_name_label(self):
		topic = Topic.objects.get(id=1)
		field_label = topic._meta.get_field('estimated_time').verbose_name
		self.assertEqual(field_label, 'Estimated Completion Time(hours)')
