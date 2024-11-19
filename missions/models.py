from django.db import models

from cats.models import Cat


class Mission(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    )

    name = models.CharField(max_length=100)
    cats = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, related_name="missions")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="PENDING")
    targets = models.ForeignKey("Target", on_delete=models.SET_NULL, null=True, related_name="missions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    status = models.CharField(max_length=100)
