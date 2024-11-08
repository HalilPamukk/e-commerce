from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from core.models import CoreModel
from django.contrib.postgres.fields import JSONField
from decimal import Decimal

class Category(CoreModel):
    """
        Product categories (e.g. Electronics, Clothing etc.)
    """
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Category Name'))
    code = models.CharField(max_length=50, unique=True, verbose_name=_('Category Code'))
    sorting = models.IntegerField(default=0, help_text=_("Used for sorting"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, 
                             help_text=_("Parent category"))
    
    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, verbose_name=_('SEO Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('SEO Description'))

    class Meta:
        ordering = ['sorting', 'name']
        unique_together = ['name', 'code']
        verbose_name_plural = _('Categories')

    def __str__(self):
        return _(self.name)

class Brand(CoreModel):
    """
        brands (e.g. Nike, Adidas)
    """
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Brand Name'))
    code = models.CharField(max_length=50, unique=True, verbose_name=_('Brand Code'))
    description = models.TextField(blank=True, verbose_name=_('Brand Description'))

    def __str__(self):
        return _(self.name)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'code']
        verbose_name_plural = _('Brands')
        

class ProductOptionKey(CoreModel):
    """
        Product option keys (e.g. Color, Size)
    """
    key = models.CharField(max_length=100, unique=True, verbose_name=_('Option Key'))
    description = models.TextField(blank=True, verbose_name=_('Option Description'))
    is_variant_creator = models.BooleanField(default=False, 
                                           help_text=_("Does this option create a new variant?"))

    def __str__(self):
        return _(self.key)

class ProductOptionValue(CoreModel):
    """
        Product option values (e.g. Red, Blue, Green)
    """
    option_key = models.ForeignKey(ProductOptionKey, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=255, verbose_name=_('Option Value'))
    sorting = models.IntegerField(default=0, verbose_name=_('Sorting'))

    class Meta:
        ordering = ['sorting']
        unique_together = ['option_key', 'value']

    def __str__(self):
        return _("%(key)s - %(value)s") % {
            'key': self.option_key.key,
            'value': self.value
        }

class MainProduct(CoreModel):
    """
        Main product -> (e.g. MacBook Pro 13")  
    """
    
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    code = models.CharField(max_length=100, unique=True, verbose_name=_('Product Code'))
    barcode = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Product Barcode'))
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    # Product Details
    description = models.TextField(blank=True, verbose_name=_('Product Description'))
    specifications = JSONField(default=dict, blank=True, verbose_name=_('Product Specifications'))
    
    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, verbose_name=_('SEO Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('SEO Description'))

    def __str__(self):
        return _(self.name)

class ProductVariants(CoreModel):
    """
        Product variants (e.g. MacBook Pro 13" - Space Gray)
    """
    name = models.CharField(max_length=255, verbose_name=_('Variant Name'))
    code = models.CharField(max_length=100, unique=True, verbose_name=_('Variant Code'))
    barcode = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=_('Variant Barcode'))
    main_product = models.ForeignKey(MainProduct, on_delete=models.CASCADE, related_name='variants')
    product_options = models.ManyToManyField(ProductOptionValue, related_name='product_variants')
    
    class Meta:
        unique_together = ['main_product', 'code']
        verbose_name = _('Product Variant')
        verbose_name_plural = _('Product Variants')

    def __str__(self):
        return _(self.name)
    
    

class ProductPrice(CoreModel):
    """
        Mainproduct -> ProductVariant -> Price (e.g. MacBook Pro 13' - Space Gray - $1299)
    """
    main_product = models.ForeignKey(MainProduct, on_delete=models.CASCADE, related_name='prices')
    variant = models.ForeignKey(ProductVariants, on_delete=models.CASCADE, related_name='prices')    
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    
    # TODO: Currency will be coming from the finance app.
    
    # TODO: Add discount

    class Meta:
        unique_together = ['product', 'variant', 'currency']
        verbose_name = _('Product Price')
        verbose_name_plural = _('Product Prices')

    def __str__(self):
        return _("%(product)s - %(variant)s - %(price)s") % {
            'product': self.main_product.name,
            'variant': self.variant.name,
            'price': self.price
        }



#TODO -> First Create a Gallery modüles and then add to the ProductImage Model.
