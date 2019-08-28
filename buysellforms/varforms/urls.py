from django.urls import path
from . import views

app_name = 'varforms'

urlpatterns = [
	path('', views.multiple_forms, name='multiple_forms'),
]