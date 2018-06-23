from django.contrib import admin
from .models import VendorDetail
from .models import VendorPost

admin.site.register(VendorDetail)

admin.site.register(VendorPost)