from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    desc = models.TextField(default="old dojo")
    state = models.CharField(max_length=2)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)


  