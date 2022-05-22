from .models import Vestido
from django.views.generic import ListView


class VestidoListView(ListView):
    model = Vestido
    template_name = "vestidos/index.html"
