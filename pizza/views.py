# Create your views here.
from pizza.serializers import *
from rest_framework import generics
from .models import *
from rest_framework import filters

class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all().prefetch_related('toppings')
    # filterset_fields = ['size']
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'size'] #,'toppings__name'

    def get_serializer_class(self):
        print(self.request.GET.get('search'))
        if self.request.method == 'GET':
            return PizzaSerializer
            # When get request get all pizzas along with nested topping objects
        if self.request.method == 'POST': 
            return PizzaSerializerSimple
            # Added PizzaSerializerSimple when post request so that we can send topping as array  
            # of primary keys of toppings (rather than entire topping objects) in post body

# This will just list out pizzas along with nested topping objects 
class PizzaListAll(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaCreate(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaRetrieve(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'id'

class PizzaUpdate(generics.UpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializerSimple
    lookup_field = 'id'

class PizzaDestroy(generics.DestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'id'



class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer