from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image_url_1 = models.URLField(null=False, blank=False)
    image_url_2 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title