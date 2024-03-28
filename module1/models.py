from django.db import models

# Create your models here.
class Sindhu(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class Meta:
        db_table="Sindhu"


class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    suggestion=models.CharField(max_length=100)
    class Meta:
        db_table="contactus"


class login(models.Model):
    username=models.CharField(max_length=100)
    pass1=models.CharField(max_length=30)
    class Meta:
        db_table="login"