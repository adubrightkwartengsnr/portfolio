from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(null = False,default="blog image")
    description = models.TextField(null= False,default="Empty Blog")
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title