from django.db import models
from django_app.models import *


class Data(models.Model):
    firm = models.ForeignKey(Advisors, related_name='advisors', null=True, on_delete=models.SET_NULL)
    data_name = models.CharField(max_length=200, null=True, blank=True, default='')
    data_check = models.BooleanField(default=False)

    class Meta:
        db_table = u'"data\".\"data"'
