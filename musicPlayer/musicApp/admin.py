from django.contrib import admin
from .models import user_auth, Music_field
# Register your models here.

admin.site.register(user_auth)
admin.site.register(Music_field)