from django.db import models
from django.utils.translation import gettext_lazy as _



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Product Name"))
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name=_("Product Price"))
    quantity_in_Stoke = models.IntegerField(verbose_name=_("Product Quantity"))

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} --> {self.quantity_in_Stoke}"