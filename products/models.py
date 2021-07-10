from django.db import models
from django.contrib.auth.models import User
from django.db import transaction


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    fa_icon_class = models.CharField(max_length=150, default='fas fa-exclamation')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Condition(models.Model):
    description = models.CharField(max_length=254)
    friendly_description = models.CharField(max_length=254)

    def __str__(self):
        return self.description

    def get_friendly_name(self):
        return self.friendly_description


class Product(models.Model):
    username = models.ForeignKey(User,
                                 null=True, blank=False,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,
                                 null=True, blank=False,
                                 on_delete=models.SET_NULL)
    measurements = models.CharField(max_length=150, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    condition = models.ForeignKey(Condition, null=True,
                                  on_delete=models.SET_NULL)
    creation_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title


class Image(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField()
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        if not self.main_image:
            return super(Image, self).save(*args, **kwargs)
        with transaction.atomic():
            Image.objects.filter(product__id=self.product.id,
                                 main_image=True).update(main_image=False)
            return super(Image, self).save(*args, **kwargs)
