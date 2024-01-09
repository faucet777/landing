from django.db import models
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    cat_tag = models.CharField(max_length=31)
    cat_name = models.CharField(max_length=63)
    cat_description = models.CharField(max_length=1023)

    def __str__(self):
        return str(self.cat_tag)

class Units(models.Model):
    unit_tag = models.CharField(max_length=31)
    unit_name = models.CharField(max_length=63)
    unit_okei = models.CharField(max_length=10, default='000', null=True, blank=True)

    def __str__(self):
        return str(self.unit_tag)



class Services(models.Model):
    serv_cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    serv_tag = models.CharField(max_length=31)
    serv_name = models.CharField(max_length=63)
    serv_description = models.CharField(max_length=2047)
    serv_unit = models.ForeignKey(Units, on_delete=models.PROTECT)
    serv_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    serv_img = models.ImageField(upload_to='services', blank=True, null=True)

    def __str__(self):
        return str(self.serv_tag)

    def get_absolute_url(self):
        return reverse('this_service', kwargs={'service_tag': self.serv_tag})


class Tickets(models.Model):
    client_email = models.EmailField()
    client_phone: models.IntegerField(max_length=11, blank=True, null=True)
    client_name = models.CharField(max_length=64, blank=True,null=True)
    ticket_subject = models.TextField(blank=True, null=True)