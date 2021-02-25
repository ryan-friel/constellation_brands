from django.db import models
from django.contrib.auth.models import User

# Import winery. One to Many relationship from reservation to Winery.
from wineries.models import Winery

class Reserveration(models.Model):

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_location = models.ForeignKey(Winery, on_delete=models.CASCADE)
    reservation_time = models.DateField()

    def __str__(self):
        return f"self.user at self.reservation.name"