from django.db import models

# Create your models here.

# Create your models here.
class Webhook(models.Model):
    company_id = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    created_at = models.CharField(max_length=500)
    updated_at = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)