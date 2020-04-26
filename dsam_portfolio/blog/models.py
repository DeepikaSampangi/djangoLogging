from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=256)
    blog_desc = models.TextField()
    blog_date = models.DateTimeField()
    blog_img = models.ImageField(upload_to='imgs/')


    def __str__(self):
        return self.blog_title

    def blog_date_pretty(self):
        return self.blog_date.strftime('%b %e %Y')


