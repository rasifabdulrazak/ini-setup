from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

class Author(BaseModel):
    name = models.CharField(max_length=555)
    place = models.CharField(max_length=555)

class Book(BaseModel):
    name = models.CharField(max_length=505)
    released_date = models.DateField()
    author_id = models.ForeignKey(Author,related_name='book_author',on_delete=models.CASCADE)
    
