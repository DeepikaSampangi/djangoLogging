from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Job(models.Model):
    job_name = models.CharField(max_length=128)
    job_img = models.ImageField(upload_to='imgs/')
    job_summary = models.CharField(max_length=512)

class TechExp(models.Model):
    techexp_name = models.CharField(max_length=256)

class booksModel(models.Model):
    book_name = models.CharField(max_length=512)
    book_author = models.CharField(max_length=512)
    book_summary = models.TextField(max_length=2048)
    book_best_quote = models.TextField(max_length=2048)
    book_rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
