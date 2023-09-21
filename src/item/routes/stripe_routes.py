from django.urls import path

from item.api.stripe_apis import GetSessionIdForItemAPIView

urlpatterns = [
    path("buy/", GetSessionIdForItemAPIView.as_view(), name="get_session_id_for_item"),
]
