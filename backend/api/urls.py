from django.urls import path

from api.views import FoodCategoryListView

app_name = 'api'

urlpatterns = [
    path('foods/', FoodCategoryListView.as_view(), name='food-list'),
]
