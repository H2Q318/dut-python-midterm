from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Item(models.Model):
    code = models.TextField(max_length=10, null=False)
    name = models.TextField(max_length=256, null=False)
    count = models.IntegerField(default=0, null=False)
    cost = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    def __str__(self):
        return f'{self.id} - {self.code} - {self.name} - {self.count} - {self.cost}'
