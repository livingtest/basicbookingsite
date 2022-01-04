from django.contrib import admin
from django.db import models


from .models import Agents, Properties,Categories,Reservation,Contact

# Register your models here.
admin.site.register(Properties)
admin.site.register(Categories)
admin.site.register(Reservation)
admin.site.register(Contact)
admin.site.register(Agents)