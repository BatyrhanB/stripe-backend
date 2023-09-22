from django.db import models

from common.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Name of Item")
    description = models.TextField(null=True, blank=True, verbose_name="Description of Item")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price of Item")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "item__items"
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ("-created_at",)
