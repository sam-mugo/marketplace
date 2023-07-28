from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    class ROLES(models.IntegerChoices):
        CUSTOMER = 0
        FARMER = 1
        LOGISTICS = 2
        ADMIN = 3
    role = models.IntegerField(choices=ROLES.choices, default=0)
    
