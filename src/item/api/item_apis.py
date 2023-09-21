from django.shortcuts import get_object_or_404
from rest_framework import views, renderers, response, generics

from item.models import Item
from item.serializers.items_serializer import ItemListSerializer


class BuyItemByIdAPIView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "buy_item.html"

    def get_queryset(self):
        return Item.objects.filter(is_deleted=False)

    def get(self, request):
        item = self.get_queryset()
        return response.Response({"item": item})


class ItemsListAPIView(generics.ListAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    serializer_class = ItemListSerializer
