from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from users.custom_modules.django_permanent.query import (
    DeletedQuerySet,
    PermanentQuerySet,
)
from users.custom_modules.django_permanent.models import PermanentModel
from users.custom_modules.django_permanent.managers import MultiPassThroughManager
from users.managers import CustomUserManager


class ServerFileQuerySet(PermanentQuerySet):
    pass


class CustomUser(AbstractUser, PermanentModel):
    class Permanent:
        restore_on_create = True

    def clean(self):
        try:
            super().clean()
            self.email = self.__class__.objects.normalize_email(self.email)
        except Exception:
            pass

    objects = MultiPassThroughManager(PermanentQuerySet, CustomUserManager)
    deleted_objects = MultiPassThroughManager(ServerFileQuerySet, DeletedQuerySet)
    all_objects = MultiPassThroughManager(ServerFileQuerySet, PermanentQuerySet)

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
