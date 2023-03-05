"""
Base models
"""
from django.db import models


class BaseModel(models.Model):
    """
    Base class model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        """
        Class meta
        """
        abstract = True
