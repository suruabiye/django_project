from django.shortcuts import render
from django.views.generic import TemplateView


# create your view here. here we use. Class-Based-View
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = 'about.html'
