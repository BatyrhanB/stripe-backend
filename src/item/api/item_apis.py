from typing import Type
from django.db.models import QuerySet
from rest_framework import views, renderers, response, generics, request

from item.models import Item
from item.serializers.items_serializer import ItemListSerializer


class BuyItemByIdAPIView(views.APIView):
    """
    API View for rendering a template with a list of items available for purchase
    """

    renderer_classes: Type[renderers.BaseRenderer] = [renderers.TemplateHTMLRenderer]
    template_name: str = "buy_item.html"

    def get_queryset(self) -> "QuerySet[Item]":
        """
        Retrieves all non-deleted items from the database

        :return: A QuerySet containing all non-deleted items
        """
        return Item.objects.filter(is_deleted=False)

    def get(self, request: request.Request) -> response.Response:
        """
        Handles GET requests, rendering a template with the available items

        :param request: The HTTP GET request
        :return: A Response object with the rendered template
        """
        item = self.get_queryset()
        return response.Response({"item": item})


class ItemsListAPIView(generics.ListAPIView):
    """
    API View for retrieving a list of all non-deleted items in JSON format
    """

    queryset = Item.objects.filter(is_deleted=False)
    serializer_class: Type[ItemListSerializer] = ItemListSerializer