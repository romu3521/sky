from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Sum

# Register your models here.
from django import forms
from .models import FoPosts
from .models import FoComments
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
    #change_list_template = "admin/basecom/foposts/model_stats.html"
    list_display=["post_title","access_count"]

    def changelist_view(self, request, extra_context=None):
        stat =  FoPosts.objects.aggregate(Sum('access_count'))["access_count__sum"]

        extra_context = extra_context or {}
        extra_context['stat'] = stat

        return super().changelist_view(request, extra_context=extra_context)

    def g_url_name(self, obj):
        return obj.url_name

    fieldsets = (

        ("タイトル", {
            'fields': ['post_title'],
        }),
        ("著者", {
            'fields': ['author_name'],
        }),
        ("許可", {
            'fields': ['is_public_article','is_public_cmt'],
        }),
        ("引用", {
            'fields': ['cite'],
        }),
        ("内容", {
            'fields': ['post_content'],
            'description': f'''
画像は:{{picX:medium}} と記述してください(サイズはsmall,medium,large)<br/>
div タグが利用できます。<br/>
class="rmmidasi1"で見出しになります！
class="attention"で補足章になります！
class="cite"で引用になります！
''',
        }),
        ('画像設定', {
            'fields': ('post_pic', 'post_pic2',"post_pic3","post_pic4","post_pic5"),
        }),
        ("URL", {
            'fields': ['url_name'],
            'description': '空白ならば日付+ランダム文字列',
        }),
    )
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        
        if obj:
            # モデルの値を動的に挿入
            custom_description = mark_safe(
                f' <a href="/post/{obj.url_name}.html" target="_blank">確認</a> '
            )
            fieldsets += (('確認', {
                'fields': (),
                'description': custom_description,
            }),)

        return fieldsets

admin.site.register(FoPosts, FoPostsAdmin)
admin.site.register(FoComments)
admin.site.register(FoContact,FoContactAdmin)
admin.site.site_header = 'romの管理サイト'
admin.site.index_title = 'romの管理サイト'
admin.site.site_title = 'romの管理サイト'
