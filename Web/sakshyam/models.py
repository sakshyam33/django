from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('Hr', 'Herbal'),
        ('Mi', 'Milk'),
        ('Gr', 'Green'),
        ('Co', 'Coffee'),
    ]
    CHAI_SIZE=[
        ('S','small'),
        ('M','medium'),
        ('L','large')
    ]
    id = models.AutoField(primary_key=True) #not done migration
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='chais/', null=True, blank=True)
    date_add = models.DateField(default=timezone.now)
    ttype = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='ML')
    size= models.CharField(max_length=1,choices=CHAI_SIZE,default='S')
    description = models.TextField(default='')
    amount = models.PositiveIntegerField(default=10)  # New field for stock amount

    def reduce_amount(self, quantity=1):
        """Decrease the stock by the specified quantity."""
        if self.amount >= quantity:
            self.amount -= quantity
            self.save()

class store(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.username} ({self.email})"
class Cart(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        chai=models.ForeignKey(ChaiVarity,on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)

        def __str__(self):
            return (f"{self.User}:{self.chai} x {self.quantity}")
class Checkout(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     full_name=models.CharField(max_length=50)
     email=models.EmailField("Email", max_length=254)
     address=models.CharField(max_length=200)
     street=models.CharField(max_length=255)
     state=models.CharField(max_length=255)
     phone = PhoneNumberField(verbose_name=_("Phone"))
    #  this hassnot been migrated
class Category(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('Hr', 'Herbal'),
        ('Mi', 'Milk'),
        ('Gr', 'Green'),
        ('Co', 'Coffee'),
        ('El','Elong'),
        ('Ma','Matcha'),
        ('Pr','Peppermint'),
    ]
    category = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='ML',verbose_name='Chai Type')
class Feedback(models.Model):
     category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Chai Type')
     feedback=models.CharField(max_length=1000,verbose_name='Your Feedback')