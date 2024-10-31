from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','Masala'),
        ('Hr','Herbal'),
        ('Mi','Milk'),
        ('Gr','Green'),
    ]
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='chais/',null=True,blank=True)
    date_add=models.DateField(default=timezone.now)
    ttype=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE,default=CHAI_TYPE_CHOICE[0])
