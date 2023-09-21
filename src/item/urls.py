from django.urls import path, include


urlpatterns = [
    path("", include("item.routes.stripe_routes"), name="stripe-routes"),
    path("", include("item.routes.item_routes"), name="item-routes"),
]