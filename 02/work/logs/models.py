from django.db import models

class WorkLog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return self.title
