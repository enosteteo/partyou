from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField('Name', max_length=255, unique=True, null=False)
    price = models.CharField('Price', max_length=255, null=False)

    def str(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('W', 'Waiting to dispatch'),
        ('D', 'Dispatched'),
    )

    # Dados do Comprador
    # client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='Order')

    # Dados específicos do Pedido
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')
    products = models.ManyToManyField(Products)

    def str(self):
        # return self.client.name
        return self.status
