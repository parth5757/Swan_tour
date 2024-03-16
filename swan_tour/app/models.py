from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    '''Base Model is here'''
    class Meta:
        abstract = True
    
    id = models.AutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    