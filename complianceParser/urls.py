from django.urls import path

from . import views

urlpatterns = [path("compliance_check", views.compliance_check, name = "compliance_check"),
               ]