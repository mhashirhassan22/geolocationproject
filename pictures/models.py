from django.db import models
# Create your models here.

class Location(models.Model):
    latitude = models.DecimalField(null=False, decimal_places=5 , max_digits=10)
    longitude = models.DecimalField(null=False, decimal_places=5 , max_digits=10)
    name = models.CharField(null=False, max_length=255)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=False,default= 0
    )

    def __str__(self):
        return self.name

class Favorites(models.Model):
    server = models.CharField(null=False,max_length=255)
    photo_id = models.CharField(null=False, max_length=255)
    secret = models.CharField(null=False,max_length=255)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=False,default= 0
    )


    def __str__(self):
        return self.photo_id
