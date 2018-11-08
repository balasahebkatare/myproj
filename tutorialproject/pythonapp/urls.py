from django.urls import path
from django.views.generic import TemplateView
#from pythonapp import views
urlpatterns=[
#python views
path('',TemplateView.as_view(template_name="pythonapp/introduction.html"), name="python_introduction"),
path('first-program/',TemplateView.as_view(template_name="pythonapp/first_program.html"), name='python_first_program'),
]
