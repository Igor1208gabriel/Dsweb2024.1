from django.urls import path
from .views import RemedioView

app_name = 'remedio'

urlpatterns = [
    path('', RemedioView.as_view(), name='remedio'),
]