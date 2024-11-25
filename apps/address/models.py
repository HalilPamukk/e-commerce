import uuid
import logging

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.models import CoreModel
from django.contrib.auth.models import User

# Create your models here.

logger = logging.getLogger(__name__)

class Region(CoreModel):
    CACHE_KEY = "region"

    name = models.CharField(
        max_length=512, verbose_name=_("Region Name"), null=True, blank=True
    )
    code = models.CharField(
        max_length=32, verbose_name=_("Region Code"), null=True, blank=True
    )

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=['name', 'code'], name='unique_region')
        ]
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return f"{self.name} - ({self.code})"
    
    def clean(self):
        """Model validation"""
        if not (self.name or self.code):
            raise ValidationError(_("Name and code are required fields."))
        
    def _json(self) -> dict:
        """Returns the model data as a dictionary. """
        return {self.__dict__}
    

class Country(CoreModel):
    CACHE_KEY = "countries"
    
    name = models.CharField(
        max_length=64, unique=True, verbose_name=_("Name")
    )
    alpha2Code = models.CharField(
        max_length=2, null=True, blank=True, verbose_name=_("Alpha 2 Code")
    )
    alpha3Code = models.CharField(
        max_length=3, null=True, blank=True, verbose_name=_("Alpha 3 Code")
    )
    calling_code = models.CharField(
        max_length=5, null=True, blank=True, verbose_name=_("Calling Code")
    )
    region = models.ForeignKey(
        "Region",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("Region"),
    )
    
    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ["name"]
        
    def __str__(self):
        return f"{self.name} - ({self.alpha2Code})"
    

class City(CoreModel):
    CACHE_KEY = "city"

    name = models.CharField(max_length=128, verbose_name=_("Name"), db_index=True)
    country = models.ForeignKey(
        "Country",
        null=True,
        blank=True,
        verbose_name=_("Country"),
        on_delete=models.PROTECT,
    )
    code = models.CharField(
        max_length=32, verbose_name=_("Code"), null=True, blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.country}"
    

class Township(CoreModel):
    CACHE_KEY = "township"

    city = models.ForeignKey("City", on_delete=models.PROTECT, verbose_name=_("City"))
    name = models.CharField(max_length=128, verbose_name=_("Name"), db_index=True)
    code = models.CharField(
        max_length=32, verbose_name=_("Code"), null=True, blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.city}"


class District(CoreModel):
    CACHE_KEY = "district"

    township = models.ForeignKey(
        "Township", on_delete=models.PROTECT, verbose_name=_("Township")
    )
    name = models.CharField(max_length=128, verbose_name=_("Name"), db_index=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.township}"
    

class Address(CoreModel):
    CACHE_KEY = "address"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, verbose_name=_("User"))
    region = models.ForeignKey(
        "Region",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("Region"),
    )
    country = models.ForeignKey(
        "Country",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("Country"),
    )
    city = models.ForeignKey(
        "City",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("City"),
    )
    township = models.ForeignKey(
        "Township",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("Township"),
    )
    district = models.ForeignKey(
        "District",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("District"),
    )
    
    # Address 
    address_title = models.CharField(max_length=128, verbose_name=_("Address Title"))
    address = models.TextField(verbose_name=_("Address"))
    postal_code = models.CharField(max_length=32, verbose_name=_("Postal Code"))
    phone = models.CharField(
        max_length=32,
        help_text=_("Ex: 530 111 1111"),
        null=True,
        blank=True,
        verbose_name=_("Phone"),
    )
    internal = models.CharField(
        max_length=16, null=True, blank=True, verbose_name=_("Internal")
    )
    first_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Last Name")
    )
    
    
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.address_title} - {self.address}"