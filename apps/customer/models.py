from django.db import models



class Customer(models.Model):
    """Customer information."""

    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    tax_id = models.TextField(blank=True, default="C/F")
    address = models.TextField(blank=True, default="Ciudad")

    def __str__(self):
        return self.name + " " + self.last_name

