from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# class Roles(models.Model):
#     role_name = models.CharField("Name", max_length=240)
#
#     def __str__(self):
#         return self.role_name
#
#     class Meta:
#         db_table = u'"django\".\"role"'


class Advisors(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, blank=True,
    )
    # user_role = models.ForeignKey(Roles, related_name='role', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = u'"django\".\"advisor"'
