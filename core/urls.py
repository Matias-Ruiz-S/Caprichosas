from django.urls import path

from .views import home, template

urlpatterns = [
    path("", home,name="home"),
    path("template.html", template,name="template"),
]

urlpatterns = [
    path("", home,name="home"),
    path("template", template,name="template"),
]