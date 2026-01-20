from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpa os dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Times
        marvel = Team.objects.create(name='marvel', description='Time Marvel')
        dc = Team.objects.create(name='dc', description='Time DC')

        # Usuários
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True)
        diana = User.objects.create(email='diana@prince.com', name='Diana Prince', team='dc', is_superhero=True)

        # Atividades
        Activity.objects.create(user=tony.name, activity_type='corrida', duration=30, date=timezone.now())
        Activity.objects.create(user=steve.name, activity_type='bicicleta', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce.name, activity_type='natação', duration=60, date=timezone.now())
        Activity.objects.create(user=diana.name, activity_type='corrida', duration=50, date=timezone.now())

        # Workouts
        Workout.objects.create(name='Supino', description='Supino reto com barra', difficulty='médio')
        Workout.objects.create(name='Agachamento', description='Agachamento livre', difficulty='difícil')
        Workout.objects.create(name='Flexão', description='Flexão de braço', difficulty='fácil')

        # Leaderboard
        Leaderboard.objects.create(user=tony.name, points=120, rank=1)
        Leaderboard.objects.create(user=steve.name, points=110, rank=2)
        Leaderboard.objects.create(user=bruce.name, points=105, rank=3)
        Leaderboard.objects.create(user=diana.name, points=100, rank=4)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
