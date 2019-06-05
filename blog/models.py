from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    begin_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Formation(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    description = models.TextField()
    institution = models.CharField(max_length=75)
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self): 
        return self.name

class Latest(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    description = models.TextField()
    institution = models.CharField(max_length=75, default="Autonomo")
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self): 
        return self.name