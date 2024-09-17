from django.db import models

# Create your models here.

class Category( models.Model): 
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)
    isbn= models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='covers/')                                        