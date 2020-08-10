from django.db import models

# Create your models here.

class Destination(models.Model):

    name= models.CharField(max_length=50,null=True)
    img= models.ImageField(upload_to='pics',null=True,blank=True)
    desc= models.CharField(max_length=50,null=True)
    price= models.IntegerField(null=True)
    offer = models.BooleanField(default=False)

