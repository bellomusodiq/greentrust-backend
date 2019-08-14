from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from products.models import Product

# Create your models here.

# revenue - Actual balance, last payment
# pending payment
# witdrawal - each witdrawal

class Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revenue_user')
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.amount)
    
class Witdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='witdrawal_user')
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.amount)

class Payment(models.Model):
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_by_user')
    payment_for = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.paid_by, self.paid_to)

@receiver(post_save, sender=Revenue)
def update_user_revenue(sender, instance, created, **kwargs):
    user = User.objects.get(pk=instance.user.pk)
    if instance.approved and created:
        if instance.pending:
            user.pending_payments += instance.amount
        else:
            user.revenue += instance.amount
        user.save()
    