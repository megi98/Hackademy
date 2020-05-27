from django.contrib import admin
from education.models import (Courses, Lectures, Tasks, Solutions)


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_duration', 'start_date', 'end_date')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.duration.days // 7} weeks'

        return 'N/A'

    get_duration.short_description = 'Duration'


@admin.register(Lectures)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'week', 'course', 'url')


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'course', 'lecture')


@admin.register(Solutions)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'url')

    def get_task_description(self, obj):
        return obj.task.description

    get_task_description.short_description = 'description'
