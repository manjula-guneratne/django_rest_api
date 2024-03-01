from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = model.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.title