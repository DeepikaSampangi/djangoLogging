from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=256)
    blog_desc = models.TextField()
    blog_date = models.DateTimeField()
    blog_img = models.ImageField(upload_to='imgs/')


