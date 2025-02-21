from django.contrib import admin

# Register your models here.
from .models import Tasks

class adminInfo(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')


admin.site.register(Tasks,adminInfo)