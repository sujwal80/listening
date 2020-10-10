from django.db import models


class user_auth(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, primary_key=True)

    def __str__(self):
        return self.name
        

class Music_field(models.Model):
    name = models.CharField(max_length=50)
    music_file = models.FileField(upload_to='')