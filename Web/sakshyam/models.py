from django.db import models
from django.utils import timezone

class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('Hr', 'Herbal'),
        ('Mi', 'Milk'),
        ('Gr', 'Green'),
        ('Co', 'Coffee'),
    ]
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='chais/', null=True, blank=True)
    date_add = models.DateField(default=timezone.now)
    ttype = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default=CHAI_TYPE_CHOICE[0])
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
    # haven't made migrations
    def __str__(self):
        return f"{self.name} ({self.email})"