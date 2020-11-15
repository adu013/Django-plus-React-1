from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    email = models.EmailField(unique=True, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
