import uuid
from django.db import models
from core.models import CoreModel
from django.utils.translation import gettext_lazy as _
from core.enums import CoreTextChoices

from address.models import Address
class GenderChoices(CoreTextChoices):
    UNKNOWN = "unknown", _("Prefer not to say")
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    

class Account(CoreModel):
    CACHE_KEY = "account"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, verbose_name=_("User"))
    # Profile
    gender = models.CharField(
        max_length=8,
        choices=GenderChoices,
        verbose_name=_("Gender"),
        default=GenderChoices.UNKNOWN,
        null=True,
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("Birth date"))
    phone = models.CharField(max_length=128, verbose_name=_("Phone"))
    is_phone_verified = models.BooleanField(default=False, verbose_name=_("Is phone verified"))
    is_email_verified = models.BooleanField(default=False, verbose_name=_("Is email verified"))
    email_verified_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Email verified at"))
    
    # address
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name=_("Address")) 
    
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        