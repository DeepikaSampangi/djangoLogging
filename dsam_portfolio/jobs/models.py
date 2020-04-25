from django.db import models


class Job(models.Model):
    job_name = models.CharField(max_length=128)
    job_img = models.ImageField(upload_to='imgs/')
    job_summary = models.CharField(max_length=512)

