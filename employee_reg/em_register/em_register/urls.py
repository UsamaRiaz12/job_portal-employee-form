"""em_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from em_register import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import em_register_view
from django.urls import path
# from .views import ApplyNowView, ExportToExcel
# from .views import ExportToExcel

urlpatterns = [
    path("admin/", admin.site.urls),
     path("em_register/",views.em_register_list),
     path('em_register/', views.em_register_view, name='em_register'),
    path("em_register/<int:id>",views.em_register_detail),
    # path('apply/', ApplyNowView.as_view(), name='apply-now'),
    # path('export-to-excel/', ExportToExcel.as_view(), name='xport_selected_to_excel'),

]

urlpatterns = format_suffix_patterns(urlpatterns)