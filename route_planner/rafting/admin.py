from django.contrib import admin
from .models import Rafting, Members, Things, Images


class RaftingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'days', 'km_on_river', 'km_from_perm', 'level', 'images')
    list_display_links = ('id', 'title', 'days', 'km_on_river', 'km_from_perm')
    search_fields = ('title', 'content')
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex')
    list_display_links = ('name',)
    search_fields = ('name', 'sex')
    list_editable = ('sex',)
    list_filter = ('name',)


class ThingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'individual', 'common', 'amount')
    list_display_links = ('title',)
    search_fields = ('title', 'individual', 'common')
    list_editable = ('individual', 'common', 'amount')
    list_filter = ('individual', 'common')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'rafting')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


admin.site.register(Rafting, RaftingAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Things, ThingsAdmin)
admin.site.register(Images, ImagesAdmin)
