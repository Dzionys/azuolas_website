from django.contrib import admin
from .models import Item, ItemType, ItemCondition, ItemState

class ItemStateInline(admin.TabularInline):
    model = ItemState
    extra = 1

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ItemCondition)
class ItemConditionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ItemStateInline,)

