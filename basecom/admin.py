from django.contrib import admin

# Register your models here.
from .models import FoPosts
from .models import FoContact
from django.db.models.functions import Lower,Upper

class FoContactAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return [Upper('created_at').desc()]

admin.site.register(FoPosts)
admin.site.register(FoContact,FoContactAdmin)
