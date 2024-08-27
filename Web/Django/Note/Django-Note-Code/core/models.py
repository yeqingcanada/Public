from django.contrib.auth.models import AbstractUser
from django.db import models

"""
1. extend user,core.user
2. create profile, store.model.customer
"""
"""
这个class User是继承django自带auth的user model,重写了一些custom的内容
AUTH_USER_MODEL = 'core.User' 需要再settings中添加这句,意味着,利用core中这个user model代替default user model
添加AUTH_USER_MODEL = 'core.User' 会造成likes.LikedItem.user field defines a relation with the model 'auth.user', which has been swapped out(换出),具体解法,参看like models
"""
"""
在进行migrate的时候会报错,这因为,我们想swap out the user model in the middle of the project
admin是之前就已经migrate的了,但是现在修改了admin的depency----core,就很麻烦。
Migration admin.0001_initial is applied before its dependency core.0001_initial on database 'default'
"""
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
