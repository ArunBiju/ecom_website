from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
secondary_category = models.CharField(max_length=100)

class PrimaryCategoryModel(models.Model):

    primary_category = models.CharField(max_length=100, null=True)
    category_header = models.ImageField(upload_to='category', null=True, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name ="Primary Category"
        verbose_name_plural ="Primary Categories"

    def __str__(self):
        return self.primary_category

    def get_absolute_url(self):
        return reverse("PrimaryCategoryModel_detail", kwargs={"pk": self.pk})

class SecondaryCategoryModel(models.Model):

    Secondary_category = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name ="Secondary Category"
        verbose_name_plural ="Secondary Categories"

    def __str__(self):
        return self.Secondary_category

    def get_absolute_url(self):
        return reverse("SecondaryCategoryModel_detail", kwargs={"pk": self.pk})



class ProductModel(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', null=False, db_index=True)
    mrp = models.IntegerField(null=False)
    selling_price = models.IntegerField(null=False)
    details = models.TextField(null=False)
    availability = models.BooleanField()
    total_stock = models.IntegerField(null=False)
    primary_category = models.ForeignKey(PrimaryCategoryModel, on_delete=models.CASCADE, null=True)
    secondary_category = models.ForeignKey(SecondaryCategoryModel, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField( upload_to='thumbnails', height_field=None, width_field=None, max_length=None, null=True)
    product_image_1 = models.ImageField( upload_to='product_image', height_field=None, width_field=None, max_length=None, null=True)
    product_image_2 = models.ImageField( upload_to='product_image', height_field=None, width_field=None, max_length=None, null=True)
    product_image_3 = models.ImageField( upload_to='product_image', height_field=None, width_field=None, max_length=None, null=True)

    class Meta:
        verbose_name = "Prduct"
        verbose_name_plural ="Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductModel_detail", kwargs={"pk": self.pk})
