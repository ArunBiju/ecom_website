from django.db import models

# Create your models here.
class HomepageImage(models.Model):

    hpimage = models.ImageField(upload_to='homepage_image', null="true", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Homepage Image"
        verbose_name_plural ="Homepage Image"

    def __str__(self):
        name='Homepage Image'
        return name

 