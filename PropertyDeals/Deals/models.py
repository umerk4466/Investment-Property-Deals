from django.db import models


# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PropertyInvestmentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, null=True,  on_delete=models.SET_NULL)
    property_investment_type = models.ForeignKey(PropertyInvestmentType, null=True,  on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    key_features = models.TextField(blank=True, null=True)
    real_price = models.CharField(null=True, blank=True, max_length=255)
    offered_price = models.CharField(null=True, blank=True, max_length=255)
    actual_price = models.CharField(max_length=255)
    bedroom = models.CharField(max_length=255)
    bathroom = models.CharField(max_length=255)
    tenure = models.CharField(max_length=255)
    epc_rating = models.CharField(null=True, blank=True, max_length=255)
    location = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    def __str__(self):
        return self.title

def get_image_filename(instance, filename):
    id = instance.property_instance.id
    return "property_images/%s" % (id) 

class PropertyImages(models.Model):
    property_instance = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return self.property_instance.title


class UkTownAndCounty(models.Model):
    town_and_county = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.town_and_county


class UkPostcode(models.Model):
    postcode = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.postcode