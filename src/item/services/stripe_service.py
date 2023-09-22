import stripe
from typing import List, Dict

from django.conf import settings

from item.models import Item


class StripeSessionService(object):
    """
    Service for interacting with Stripe API to create sessions for items
    """
    
    __secret_key: str = settings.STRIPE_SECRET_KEY
    __item_model: Item = Item

    @classmethod
    def _generate_price_data(cls, items: List[Item]) -> List[Dict]:
        """
        Generates price data dictionary for each item in the items list
        
        :param items: List of Item objects for which to generate price data
        :return: List of dictionaries containing price data for each item
        """

        price_data = []
        for item in items:
            price_data.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": int(item.price * 100),
                    },
                    "quantity": 1,
                }
            )
        return price_data

    @classmethod
    def _get_items_by_ids(cls, item_ids: List[int]) -> List[Item]:
        """
        Retrieves items from the database by their ids
        
        :param item_ids: List of ids of the items to retrieve
        :return: List of Item objects corresponding to the given ids
        """

        return cls.__item_model.objects.filter(id__in=item_ids)

    @classmethod
    def get_session(cls, items_ids: List[int]) -> str:
        """
        Creates a Stripe checkout session and returns its id
        
        :param items_ids: List of ids of the items to include in the session
        :return: Id of the created Stripe checkout session
        """

        items = cls._get_items_by_ids(items_ids)
        price_data = cls._generate_price_data(items)

        session = stripe.checkout.Session.create(
            api_key=cls.__secret_key,
            line_items=price_data,
            mode="payment",
            success_url=settings.STRIPE_SUCCESS_URL,
            cancel_url=settings.STRIPE_CANCEL_URL, 
        )
        return session.id
