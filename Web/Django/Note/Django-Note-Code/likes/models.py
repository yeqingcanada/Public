from django.db import models
# from django.contrib.auth.models import User
"""
由于重新设置了default auth user model,需要重新import user。
这样一来,like这个app就不是独立的了,它需要依附于core这个app
但是core app is not supposed to be reusable, it implements features very specific to this project
so we don't want to explicitly import this user here
"""
# from core.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
