from django.contrib import admin
from .models import Item, ItemType, ItemCondition

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ItemCondition)
class ItemConditionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

