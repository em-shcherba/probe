from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
