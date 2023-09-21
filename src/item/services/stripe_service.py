import stripe

from django.conf import settings

from item.models import Item


class StripeSessionService(object):
    __secret_key = settings.STRIPE_SECRET_KEY
    __item_model = Item

    @classmethod
    def _generate_price_data(cls, items):
        price_data = []
        for item in items:
            price_data.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price * 100),
                },
                "quantity": 1,
            })
        return price_data

    @classmethod
    def _get_items_by_ids(cls, item_ids):
        return cls.__item_model.objects.filter(id__in=item_ids)

    @classmethod
    def get_session(cls, items_ids):
        stripe.api_key = cls.__secret_key
        items = cls._get_items_by_ids(items_ids)
        price_data = cls._generate_price_data(items)
        
        session = stripe.checkout.Session.create(
            line_items=price_data,
            mode="payment",
            success_url="http://localhost:4242/success",
            cancel_url="http://localhost:4242/cancel",
        )
        return session.id
