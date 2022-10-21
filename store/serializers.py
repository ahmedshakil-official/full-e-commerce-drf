from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    # For getting collection ID
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )

    # For getting string representation of collection
    # collection = serializers.StringRelatedField()

    # For getting nested object of collection
    # collection = CollectionSerializer()

    # For create a hyperlink of collection
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name= 'collection-detail'
    )

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)
