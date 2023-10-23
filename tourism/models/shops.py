from django.db import models

from business import models as BMdl

class ShopModel(models.Model):
    org = models.ForeignKey(BMdl.Org, on_delete=models.CASCADE, verbose_name='Organization')
    name = models.CharField(max_length=60, verbose_name='Shop Name')
    shop_no = models.CharField(max_length=15, verbose_name='Shop No.')
    contact_no = models.CharField(max_length=15, verbose_name='Contact No.')
    # location
    lat = models.CharField(max_length=30, verbose_name='Latitude')
    lon = models.CharField(max_length=30, verbose_name='Longitude')
    # open/close status
    is_open = models.BooleanField(default=False, verbose_name='Open')
    # shop is orperational
    is_active = models.BooleanField(default=False, verbose_name='Active')
    # shop verified by following SOPs
    is_verified = models.BooleanField(default=False, verbose_name='Verified')
    # payments
    is_cash = models.BooleanField(default=False, verbose_name='Cash')
    is_card = models.BooleanField(default=False, verbose_name='Card')
    is_upi = models.BooleanField(default=False, verbose_name='UPI')
    # message
    msg = models.TextField(blank=True, null=True, verbose_name='Message')
    
    class Meta:
        abstract = True
