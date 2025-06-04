from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    sport = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=40)

    class Meta:
        db_table = 'students'


