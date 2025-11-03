from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
	def test_team_create(self):
		t = Team.objects.create(name='Test Team')
		self.assertEqual(t.name, 'Test Team')

	def test_activity_create(self):
		a = Activity.objects.create(user='test', type='run', duration=10)
		self.assertEqual(a.type, 'run')

	def test_leaderboard_create(self):
		l = Leaderboard.objects.create(user='test', score=42)
		self.assertEqual(l.score, 42)

	def test_workout_create(self):
		w = Workout.objects.create(name='Pushups', difficulty='Easy')
		self.assertEqual(w.difficulty, 'Easy')
