from django.contrib import admin


from item.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_display_links = ("name",)
    fields = (
        "name",
        "description",
        "price",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["name", "description"]
    ordering = ["-created_at"]
    list_per_page = 25