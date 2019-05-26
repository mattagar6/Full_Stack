from django.db import models

# Create your models here.
class User(models.Model):

    firstName = models.CharField(max_length = 264, unique = True)
    lastName = models.CharField(max_length = 264, unique = True)
    email = models.EmailField(max_length = 264, unique = True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
