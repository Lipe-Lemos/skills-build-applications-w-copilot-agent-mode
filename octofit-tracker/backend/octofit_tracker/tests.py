from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='marvel', is_superhero=True)
        self.assertEqual(user.email, 'test@hero.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel Team')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', activity_type='run', duration=30, date='2026-01-20')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='Test Hero', points=100, rank=1)
        self.assertEqual(lb.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        self.assertEqual(workout.difficulty, 'easy')
