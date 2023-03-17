from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)
    brand_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return self.title

class Size(models.Model):
    item = models.ForeignKey(Item, related_name='size', on_delete=models.CASCADE)
    title = models.CharField(max_length=5)

    class Meta:
        ordering = ['size']
        indexes = [
            models.Index(fields=['size'])
        ]

    def __str__(self):
        return self.title

class Price(models.Model):
    price = models.PositiveIntegerField()
    size = models.ForeignKey(Size, related_name='price', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated, -created']
        indexes = [
            models.Index(fields=['-updated', '-created'])
        ]

    def __str__(self):
        return self.price
