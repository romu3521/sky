from django.contrib import admin

# Register your models here.
from .models import FoPosts
from .models import FoContact
from django.db.models.functions import Lower,Upper

class FoContactAdmin(admin.ModelAdmin):
    list_display=["contact_mail","short_text"]
    def short_text(self, obj):
        return obj.contact_content[0:80]+"..."

    short_text.short_description = 'content'
    def get_ordering(self, request):
        return [Upper('created_at').desc()]

admin.site.register(FoPosts)
admin.site.register(FoContact,FoContactAdmin)
admin.site.site_header = 'romの管理サイト'
admin.site.index_title = 'romの管理サイト'
admin.site.site_title = 'romの管理サイト'
