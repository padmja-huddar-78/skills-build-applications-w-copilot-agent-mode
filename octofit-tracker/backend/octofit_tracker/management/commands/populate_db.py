from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        workout2 = Workout.objects.create(name='Strength Training', description='Build muscle and strength')
        workout1.suggested_for.set([marvel, dc])
        workout2.suggested_for.set([marvel])

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
