import uuid

from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from core.cache import BaseCache
from django.contrib.auth.models import User


# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name=_("Name"))
    native_name = models.CharField(max_length=32, verbose_name=_("Native Name"))
    flag = models.CharField(
        max_length=512,
        verbose_name=_("Flag"),
        help_text=_("Flag Url, example: https://restcountries.eu/data/tur.svg"),
    )
    iso639_1 = models.CharField(max_length=2, verbose_name=_("ISO639_1"))
    iso639_2 = models.CharField(max_length=3, verbose_name=_("ISO639_2"))
    # this means system
    is_system_language = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.native_name)

    class Meta:
        ordering = ["name"]

    def _json(self):
        return {
            "id": self.id,
            "name": self.name,
            "native_name": self.native_name,
            "flag": self.flag,
            "iso639_1": self.iso639_1,
            "iso639_2": self.iso639_2,
        }

    @staticmethod
    def get_available_languages():
        cache = BaseCache()
        key = "lang-cache"
        cache_value = cache._get_cache(key)
        if cache_value or cache_value == []:
            return cache_value

        result = []
        for language in Language.objects.filter(is_system_language=True):
            result.append(language._json())

        cache._set_cache(key, result, timeout=60 * 60)
        return result
    

class CoreModel(models.Model, BaseCache):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
        verbose_name=_("Created By"),
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name=_("Updated At")
    )
    updated_by = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_updated_by",
        verbose_name=_("Updated By"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Deleted At")
    )
    deleted_by = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_deleted_by",
        verbose_name=_("Deleted By"),
    )
    data = JSONField(null=True, blank=True, default=dict)
    # objects = CoreManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True
        ordering = ["id"]
    
    def save(self, user=None, *args, **kwargs):
        # TODO: The `deleted_by` field should be populated upon soft delete.
        if isinstance(self.id, int):
            if not self.id:
                if user:
                    self.created_by = user
            else:
                if user:
                    self.updated_by = user
        elif isinstance(self.id, uuid.UUID):
            """
            UUIDs are assigned during object instantiation, which means that checking `self.pk` in the
            `save` method does not reliably distinguish between new and existing instances.
            The reason is that `self.pk` will be set to a UUID for both new and existing instances,
            as the UUID is generated before the object is saved to the database.
            """
            if not self.id:
                if user:
                    self.created_by = user
            else:
                # The false branch will always be executed because the condition `not self.id` is always false.
                # Since the condition is never met, the `if` block will never run.

                # TODO: Fix the issue where the `created_user` field is not populated correctly
                # when the primary key (`id`) is a UUID.
                if user:
                    self.updated_by = user

        super().save(*args, **kwargs)
        
    def deactive(self, user:User):
        from django.utils import timezone
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.deleted_by = user
        self.save(user=user)
        
        return self
    
    
    def activate(self, user:User):
        from django.utils import timezone
        self.is_active = True
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None
        self.updated_at = timezone.now()
        self.updated_by = user
        self.save(user=user)
        