from rest_framework import serializers
from .models import Product



class Product_Serializer(serializers.ModelSerializer):
    quantity_in_Stoke = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ["name", "price", "quantity_in_Stoke"]