from django.db import models

# Create your models here.
class regdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    Image = models.ImageField(upload_to="user_img", null=True, blank=True)



class product(models.Model):

    P_cata = models.CharField(max_length=50, null=True, blank=True)
    P_name = models.CharField(max_length=50, null=True, blank=True)
    P_quantity = models.CharField(max_length=50, null=True, blank=True)
    P_number = models.IntegerField(null=True, blank=True)
    P_location = models.CharField(max_length=500, null=True, blank=True)
    P_price = models.CharField(max_length=500, null=True, blank=True)
    P_description = models.CharField(max_length=500, null=True, blank=True)
    P_sdescription = models.CharField(max_length=400, null=True, blank=True)
    P_image1 = models.ImageField(upload_to="B_product", null=True, blank=True)
    P_image2 = models.ImageField(upload_to="B_product", null=True, blank=True)
    P_image3 = models.ImageField(upload_to="B_product", null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    P_shopname = models.CharField(max_length=50, null=True, blank=True)
    P_localarea = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.P_name}"


class sam(models.Model):
    P_image1 = models.ImageField(upload_to="B_product/", null=True, blank=True)
    P_image2 = models.ImageField(upload_to="B_product/", null=True, blank=True)
    P_image3 = models.ImageField(upload_to="B_product/", null=True, blank=True)
