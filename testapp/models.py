from django.db import models

# Create your models here.
class userAuth(models.Model):
  userId = models.AutoField(primary_key = True)
  userName = models.CharField(max_length= 100 )
  userPassWord = models.CharField(max_length= 20)
