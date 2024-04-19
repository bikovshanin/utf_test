from rest_framework import generics

from api.serializers import FoodListSerializer
from menu.models import FoodCategory


class FoodCategoryListView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()
    serializer_class = FoodListSerializer
