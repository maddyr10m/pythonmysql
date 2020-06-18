from django.db import models
from django.utils import timezone
from django.contrib import messages
# Create your models here.


class GenBurnRate(models.Model):
    # this wont be added to the database must inherit first see below
    # this is abstract class inheritance

    myitem = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BurnRate(GenBurnRate):
    pub_date = models.DateField()
    paymethod = models.CharField(max_length=7)
    # def __str__(self):
    #    return self.myitem     this is for the ADMIN only


class BurnDetail(GenBurnRate):

    count_item = models.SmallIntegerField(default=1)
    itemclass = models.CharField(max_length=16)
    spendgroup = models.CharField(max_length=16)
    gengroup = models.CharField(max_length=16)
    taxrate = models.DecimalField(max_digits=5, decimal_places=4, default=0.00)
    costwithtax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fkey = models.ForeignKey(BurnRate, on_delete=models.CASCADE)