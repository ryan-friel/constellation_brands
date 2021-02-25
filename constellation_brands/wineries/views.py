from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Winery

class Home(LoginRequiredMixin, ListView):
    template_name = 'wineries/home.html'
    model = Winery