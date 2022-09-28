from django.db import models

class User(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carName = models.CharField(max_length=150)
    carModel = models.CharField(max_length=150)
    carColor = models.CharField(max_length=150)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carName
