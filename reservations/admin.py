from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservation)
class ReservatiopnAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    pass
