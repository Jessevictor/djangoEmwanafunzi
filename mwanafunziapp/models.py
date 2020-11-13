from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
# CATEGORY_CHOICES = (
#     ('S', 'Stationery'),
#     ('U', 'Uniforms'),
#     ('T', 'Toileteries'),
#     ('B', 'Books'),
#     ('F', 'Snacks')
# )
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    # imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
