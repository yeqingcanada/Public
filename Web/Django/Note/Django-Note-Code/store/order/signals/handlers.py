from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Customer

"""we use signals to decouple our apps and prevent them from stepping on each other's toes"""
"""our models have a bunch of signals or notifications that are fired at different times. for example, we have pre save that is fired before a model is saved. we also have post save which is fired after a model is saved. and we also have pre delete and post delete. so in our application we can listen to this notifications and do something"""
"""原本想在core user UserCreateSerializer处save方法下,直接新建一个customer。但是这样的话,就需要在field处写birth day等,感觉一个serializer干了两件事"""

"""下面第一行,意思是,当core user post后,trigger这个方法"""


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])


"""还需要再app.py中加一句话"""
