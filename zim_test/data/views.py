from .models import Data
from rest_framework import generics
from .serializers import DataSerializer
from django_app.models import Advisors
from django.db import connection
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist


class DataList(generics.ListAPIView):
    """
    API endpoint that allows data to be viewed.
    """

    def get_queryset(self):
        try:
            firm = Advisors.objects.get(user_id=self.request.user.id)
        except ObjectDoesNotExist:
            firm = None

        with connection.cursor() as cursor:
            if firm:
                cursor.execute(f'SET rls.advn = {firm.id}')
            else:
                raise PermissionDenied("You have no access to this data")

        return Data.objects.all()
    serializer_class = DataSerializer
