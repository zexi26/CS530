from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
	path('add/<int:product_id>/', views.add_event, name='add_event'),
	path('', views.event_detail, name='event_detail'),
	path('remove/<int:product_id>/', views.event_remove, name='event_remove'),
	path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
]