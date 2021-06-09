from django.db import models

# Create your models here.


class SourceDB(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return f"{self.name}"


class DestinationDB(models.Model):
    name = models.CharField(unique=True, max_length= 200)


    def __str__(self):
        return f"{self.name}"


class Credentials(models.Model):
    username = models.CharField( max_length= 200)
    password = models.CharField( max_length= 200)
    hostname = models.CharField(max_length= 200)
    dbname = models.ForeignKey(SourceDB, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"