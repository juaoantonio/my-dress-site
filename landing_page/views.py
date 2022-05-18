from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Vestido


class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"


