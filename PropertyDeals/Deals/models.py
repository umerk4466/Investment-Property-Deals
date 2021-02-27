from django.db import models

# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title