from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FoodGroupsPageView(TemplateView):
    template_name = 'foodgroups.html'

class MealsPageView(TemplateView):
    template_name = 'meals.html'

class SnacksPageView(TemplateView):
    template_name = 'snacks.html'