from django.contrib import admin

# Register your models here.
from django import forms
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


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = FoPosts
        fields = '__all__'
        widgets = {
            'post_content': forms.Textarea(attrs={'rows': 50, 'cols': 100}),
        }


class FoPostsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    fieldsets = (

        ("URL", {
            'fields': ['url_name'],
            'description': '必ず記述',
        }),
        ("タイトル", {
            'fields': ['post_title'],
        }),
        ("著者", {
            'fields': ['author_name'],
        }),
        ("内容", {
            'fields': ['post_content'],
            'description': '画像は:{picX:medium} と記述してください(サイズはsmall,medium,large)',  # 説明文を追加
        }),
        ('画像設定', {
            'fields': ('post_pic', 'post_pic2',"post_pic3"),
        }),
    )

admin.site.register(FoPosts, FoPostsAdmin)




#admin.site.register(FoPosts)
admin.site.register(FoContact,FoContactAdmin)
admin.site.site_header = 'romの管理サイト'
admin.site.index_title = 'romの管理サイト'
admin.site.site_title = 'romの管理サイト'
