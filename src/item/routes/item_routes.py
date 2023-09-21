from django.urls import path

from item.api.item_apis import BuyItemByIdAPIView, ItemsListAPIView

urlpatterns = [
    path("item/list/", ItemsListAPIView.as_view(), name="items_list"),
    path("item/buy/", BuyItemByIdAPIView.as_view(), name="buy_item_by_id"),
]
