from django.contrib import admin

# Register your models here.
from .models import Class, Hotel, Travel

admin.site.register([Class, Hotel, Travel])
