from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Reserveration
from .forms import ReservationForm

class Home(LoginRequiredMixin, ListView):
    template_name = "reservations/home.html"
    model = Reserveration

    def get_queryset(self):
        """
        # (R. Friel - February 25, 2021)
        Ensure only the user's reservations are returned.
        """
        return Reserveration.objects.filter(user=self.request.user)


class CreateReservation(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "reservations/create.html"
    model = Reserveration

    form_class = ReservationForm

    success_url = reverse_lazy("reservations:home")
    success_message = "Your reservation has been created."

    def form_valid(self, form):
        """
        # (R. Friel - February 25, 2021)
        Ensure that the user is added to the form so the association between user and reservation is made.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateReservation(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "reservations/update.html"
    model = Reserveration

    form_class = ReservationForm

    success_url = reverse_lazy("reservations:home")
    success_message = "You successfully saved changes to your reservation."


class DetailReservation(LoginRequiredMixin, DetailView):
    template_name = "reservations/detail.html"
    model = Reserveration
    form_class = ReservationForm


class DeleteReservation(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "reserveations/delete.html"
    model = Reserveration
    success_url = reverse_lazy("reservations:home")
    success_message = "Your selected reservation has been deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteReservation, self).delete(request, *args, **kwargs)