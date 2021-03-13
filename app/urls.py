# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.EmployeeCountView.as_view(), name='home'),

    # re_path(r'^.*\.*', views.pages, name='pages'),
    path("employees/", views.EmployeeListView.as_view(), name='employees'),
    path("filter/", views.FilterEmployeeView.as_view(), name='filter'),
    path("employee/<int:pk>/", views.EmployeeDetailView.as_view(), name='detail'),
    path("search/", views.Search.as_view(), name='search'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]
