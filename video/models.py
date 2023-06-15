from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=128)
    otp =  models.BigIntegerField(null=True)
    class Meta:
        db_table = 'register'


