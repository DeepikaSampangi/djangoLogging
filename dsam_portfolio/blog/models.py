from django.db import models


class Blog(models.Model):

    blog_title = models.CharField(max_length=128)
    blog_desc = models.CharField(max_length=2048)
    blog_img = models.ImageField(upload_to='imgs/')


