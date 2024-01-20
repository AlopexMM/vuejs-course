from django.db import models

# Create your models here.
class Dollar(models.Model):
    date = models.DateField()
    source = models.CharField(max_length=10)
    value_sell = models.DecimalField(decimal_places=2, max_digits=15)
    value_buy = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return f"{self.source}:\n {self.value_sell}"
