from django.urls import include, path
from .views import *


urlpatterns = [
    path('', DataList.as_view()),

]