from django.contrib import admin

# Register your models here.
from .models import reCommList

admin.site.site_header = 'tutorial'
admin.site.site_title = 'ttt'
@admin.register(reCommList)
class reCommListAdimin(admin.ModelAdmin):
    list_display = ['id','commId','reCommId','commTitle','commContent','commCtime','commMtype','commPhone','imgUrl']

    list_editable = ['commId', 'commTitle']

    list_display_links = ['id']

    list_filter = ['id']

    search_fields = ['commId']
