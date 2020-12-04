from rest_framework import serializers
from .models import *


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'
        
class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True,required=False)
    class Meta:
        # ordering = ['-id']
        model = Pizza
        fields = ['id', 'type', 'size', 'toppings']

# No nesting
class PizzaSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'type', 'size', 'toppings']

