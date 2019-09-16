from django.db import models

# Create your models here.
class Book(models.Model):
    # Simple Text field:Charfield
    title = models.CharField(blank = False, unique = True, null = False, max_length = 256)
    description = models.TextField(max_length = 256, blank = True)
    price = models.DecimalField(default=0, decimal_places = 2, max_digits = 123)
    published = models.TimeField(auto_now = True)
    cover = models.ImageField(upload_to = 'covers/',default = False)
    isPublished = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title