from django.contrib import admin

from .models import Footer, Col, Item, Banner
# Register your models here.
class ColInline(admin.TabularInline):
    model = Col
    fields = ('title',)

class ItemInline(admin.TabularInline):
    model = Item
    fields = ('name', 'url')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ColInline]

@admin.register(Col)
class ColAdmin(admin.ModelAdmin):
    list_display = ('title', 'footer')
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'col')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)