from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    @property
    def duration(self):
        return (self.end_date - self.start_date).days // 7

    def __str__(self):
        return self.name


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
