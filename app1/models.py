from django.db import models

# Create your models here.
class categoryA(models.Model):

    A_categoryname = models.CharField(max_length=50, null=True, blank=True)
    A_description = models.CharField(max_length=500, null=True, blank=True)
    A_image = models.ImageField(upload_to="A_category", null=True, blank=True)



