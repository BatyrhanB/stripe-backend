from rest_framework import generics, permissions, response, status, request

from item.services.stripe_service import StripeSessionService
from item.models import Item
from typing import List, Type, Any


class GetSessionIdForItemAPIView(generics.CreateAPIView):
    """
    API View to retrieve a session ID from Stripe for a given list of items
    This view allows any permissions and only works with non-deleted items
    """

    permission_classes: Type[permissions.BasePermission] = [permissions.AllowAny]
    queryset = Item.objects.filter(is_deleted=False)

    def post(self, request: request.Request, *args: Any, **kwargs: Any) -> response.Response:
        """
        Handles POST requests to create a Stripe session and return its ID

        :param request: The HTTP POST request. The request data should
                        include a list of item ids under the key "items"
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        :return: A Response object with the created session ID and a
                 HTTP 200 OK status
        """
        items: List[int] = request.data.get("items", [])
        session_id: str = StripeSessionService.get_session(items)
        return response.Response(
            {"session_id": session_id},
            status=status.HTTP_200_OK,
        )
