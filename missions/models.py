from django.db import models
from rest_framework.exceptions import ValidationError

from cats.models import Cat


class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, related_name="missions")
    is_complete = models.BooleanField(default=False)
    targets = models.ManyToManyField("Target", related_name="missions", blank=True)

    def clean(self):
        if self.targets.count() > 3:
            raise ValidationError("A mission can have a maximum of 3 targets.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_complete = models.BooleanField(default=False)
