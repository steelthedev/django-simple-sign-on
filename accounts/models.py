from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Q




class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)


    USERNAME_FIELD = "username"
    EMAIL_FIELD ="email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
