from django.urls import path
from testapp import views
urlpatterns=[
path('', views.HomeView.as_view(), name="home"),
path('educational/', views.educational, name='educational'),
path('electronics/', views.electronics, name='electronics')
]
