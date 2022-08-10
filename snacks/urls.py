from django.urls import path
from .views import HomePageView,AboutPageView,FoodGroupsPageView,MealsPageView,SnacksPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('foodgroups', FoodGroupsPageView.as_view(), name='foodgroups'),
    path('meals', MealsPageView.as_view(), name='meals'),
    path('snacks', SnacksPageView.as_view(), name='snacks'),
]
