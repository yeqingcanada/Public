from django.dispatch import receiver
from store.order.signals import order_created

@receiver(order_created)
def on_order_created(sender, **kwargs):
  """this is the keyword argument that we passed on firing this signal"""
  print(kwargs['order'])