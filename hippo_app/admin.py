from django.contrib import admin
from .models import DestinationDB, SourceDB, Credentials


# Register your models here.


admin.site.register(DestinationDB)
admin.site.register(SourceDB)
admin.site.register(Credentials)

