from django.db import models
import  datetime
# Create your models here.
class Database(models.Model):
            text = models.TextField()
            price = models.IntegerField()
            company = models.CharField(max_length=100, default="")
            purchase_date = models.DateField(default=datetime.date.today)
            quantity = models.IntegerField(default=0)
