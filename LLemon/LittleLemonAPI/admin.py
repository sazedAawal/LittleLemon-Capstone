from django.contrib import admin
from .models import LLAPIMenuItem, LLAPIMenu

admin.site.register(LLAPIMenu)
admin.site.register(LLAPIMenuItem)
