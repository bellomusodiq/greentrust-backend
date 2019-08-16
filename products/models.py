from django.db import models
from accounts.models import User
from payments.models import Revenue, RevenueType
# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.product.title

class Order(models.Model):
    order_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    approved_by_buyer = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title


@receiver(post_save, sender=Order)
def actions_after_order(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        user = instance.user
        product.active = False
        product.save()
        revenue_type = RevenueType.objects.get(name="ByOrder")
        Revenue.objects.create(user=product.created_by, revenue_type=revenue_type, amount=product.amount)
