from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('instagram_id', 'text', 'owner', 'publish_date')
    list_filter = ('instagram_id', 'owner')
    search_fields = ('instagram_id', 'text', 'owner', 'publish_date')
