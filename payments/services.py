import stripe

from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


class StripePaymentManager:

    def __init__(self, price_value, course_id):
        self.success_url = "http://127.0.0.1:8000/"
        self.price_value = price_value
        self.course_id = course_id

    def create_stripe_product(self):
        return stripe.Product.create(name="Course subscription")

    def create_stripe_price(self, product):
        return stripe.Price.create(
            currency="rub",
            unit_amount=self.price_value * 100,
            product_data={"name": product.get("id")},
        )

    def create_stripe_session(self, price):
        session = stripe.checkout.Session.create(
            success_url=self.success_url,
            line_items=[
                {"price": price.get("id"), "quantity": 1},
            ],
            mode="payment",
        )
        return session.get("id"), session.get("url")

    def process_payment(self):

        product = self.create_stripe_product()
        price = self.create_stripe_price(product)
        return self.create_stripe_session(price)
