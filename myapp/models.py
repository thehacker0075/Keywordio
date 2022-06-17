from distutils.command import upload
from importlib.util import module_for_loader
from pyexpat import model
from random import choices
from secrets import choice
from django.db import models

# Create your models here.
class Admin(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.fname

class Book(models.Model):
    CHOICE1=(
        ('coding_book','coding_book'),
        ('hacking_book','hacking_book'),
        ('history_book','history_book'),
        ('general_knowledge','general_knowledge'),
    )

    admin_book=models.ForeignKey(Admin,on_delete=models.CASCADE)
    book_collection=models.CharField(max_length=100,choices=CHOICE1)
    book_name=models.CharField(max_length=100)
    book_price=models.CharField(max_length=100)
    book_des=models.TextField()
    book_image=models.ImageField(upload_to="book_image/")

    def __str__(self):
        return self.admin_book.fname+" - "+self.book_collection+" - "+self.book_name