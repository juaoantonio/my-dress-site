from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Vestido


class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"


class VestidoListView(ListView):
    model = Vestido
    template_name = "landing_page/vestidos.html"

