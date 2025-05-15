# models/payment.py
import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_your_test_key_here")  # fallback if env missing

class Payment:
    def __init__(self, user, amount):
        self.user = user
        self.amount = int(amount * 100)  # Convert to cents (Stripe requires)

    def process_payment(self):
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "DevMart Purchase",
                            "description": f"Order by {self.user.name}",
                        },
                        "unit_amount": self.amount,
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url="https://example.com/success",  # Replace with your site
                cancel_url="https://example.com/cancel",    # Replace with your site
                customer_email=self.user.email
            )
            return session.url  # Stripe-hosted checkout page link
        except Exception as e:
            print("Stripe error:", e)
            return None


from dotenv import load_dotenv
load_dotenv()
