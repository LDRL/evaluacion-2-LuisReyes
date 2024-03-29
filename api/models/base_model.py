"""Django models utilities"""

# Django
from django.db import models


class BaseModel(models.Model):
    """
    """

    created = models.DateTimeField('created at', auto_now_add=True,
                                   help_text='Date time on wich the object was created.')
    modified = models.DateTimeField('modified at', auto_now=True,
                                    help_text='Date time on wicht the object was last modified')

    class Meta:
        """Meta option"""
 
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']