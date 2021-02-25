from django import forms

from .models import Reserveration

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reserveration
        fields = [
            "reservation_location",
            "reservation_time"
        ]
