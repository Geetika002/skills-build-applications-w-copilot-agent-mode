
from djongo import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
	user = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()

class Leaderboard(models.Model):
	user = models.CharField(max_length=100)
	score = models.IntegerField()

class Workout(models.Model):
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
