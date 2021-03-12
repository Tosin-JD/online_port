from django.urls import path
from .views import ServiceList, ServiceDetail


app_name = 'services'


urlpatterns = [
        path('', ServiceList.as_view(), name='all'),
        path('<int:pk>/', ServiceDetail.as_view(), name='detail'),
    ]



