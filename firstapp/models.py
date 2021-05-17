from django.db import models  


class Register(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    password = models.CharField(max_length=20)
    class Meta:
        db_table = "registers"
class Birthday(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    rate = models.IntegerField()
    class Meta:
        db_table = "birthday"
class Anniversary(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    rate = models.IntegerField()
    class Meta:
        db_table = "anniversary"

class Book(models.Model):
    username = models.CharField(max_length=80)
    ename = models.CharField(max_length=80)
    price = models.IntegerField()
    phnno = models.IntegerField()
    
    class Meta:
        db_table = "bookingdetails"
