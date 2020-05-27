from django.db import models
from django.utils import timezone
from .validate_url import validator


class Courses(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course {self.name}'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lectures(models.Model):
    name = models.CharField(max_length=50)
    week = models.IntegerField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Solutions(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    url = models.URLField(validators=[validator])

    def __str__(self):
        return f'Solution for task {self.task}'
