from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
