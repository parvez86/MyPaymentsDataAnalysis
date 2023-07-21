from django.contrib import admin
from .models import App, Sdk, AppSdk


class AppAdmin(admin.ModelAdmin):
    # list_filter = ('name', 'company_url', 'genre_id', 'release_date', 'seller_name', 'artwork_large_url')
    list_display = ('id', 'company_url', 'name', 'genre_id', 'release_date', 'seller_name', 'artwork_large_url')
    list_filter = ['id', 'name']
    search_fields = ['name', 'company_url', 'genre_id', 'release_date', 'seller_name', 'artwork_large_url']


class SdkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url', 'description')
    search_fields = ('id', 'name', 'slug', 'url', 'description')
    list_filter = ['id', 'name']


class AppSdkAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_id', 'sdk_id', 'installed')
    search_fields = ('id', 'app_id', 'sdk_id', 'installed')
    # list_filter = ['id']


# Register your models here.
admin.site.register(App, AppAdmin)
admin.site.register(Sdk, SdkAdmin)
admin.site.register(AppSdk, AppSdkAdmin)