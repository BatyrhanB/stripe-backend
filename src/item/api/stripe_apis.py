from rest_framework import generics, permissions, response, status

from item.services.stripe_service import StripeSessionService
from item.models import Item


class GetSessionIdForItemAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.filter(is_deleted=False)

    def post(self, request, *args, **kwargs):
        items = request.data.get("items", [])
        session_id = StripeSessionService.get_session(items)
        return response.Response(
            {"session_id": session_id},
            status=status.HTTP_200_OK,
        )
