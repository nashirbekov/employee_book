# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
import datetime
from django.shortcuts import render
from django.db.models import Count

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .permissions import UserPermissionMixin
from app.forms import AuthUserForm, RegisterUserForm
from app.models import Employee, City, WorkStatus


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


class EmployeeListView(ListView):
    """Список сотрудников"""
    model = Employee
    queryset = Employee.objects.all()
    template_name = "tables.html"
    paginate_by = 2

    def get_cities(self):
        return City.objects.all()

    def get_work_status(self):
        return WorkStatus.objects.all()


class FilterEmployeeView(EmployeeListView, ListView):
    """Фильтр сотрудников"""
    paginate_by = 2

    def get_queryset(self):
        queryset = Employee.objects.filter(
            Q(city__in=self.request.GET.getlist("city")) |
            Q(work_status__in=self.request.GET.getlist("work_status"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["city"] = ''.join([f"city={x}&" for x in self.request.GET.getlist("city")])
        context["work_status"] = ''.join([f"work_status={x}&" for x in self.request.GET.getlist("work_status")])
        return context


class EmployeeDetailView(PermissionRequiredMixin, DetailView):
    """Подробная инфа о сотруднике"""
    permission_required = 'app.view_employee'
    model = Employee
    template_name = "employee_detail.html"

    def count_date(self):
        today = datetime.date.today()
        employment_date = self.object.employment_date
        date_of_dismissal = self.object.date_of_dismissal
        if date_of_dismissal:
            work_experience = (date_of_dismissal - employment_date).days // 7
        else:
            work_experience = (today - employment_date).days // 7

        work_experience = str(work_experience) + ' weeks'
        return work_experience


class Search(LoginRequiredMixin, ListView):
    """Поиск сотрудников"""
    paginate_by = 2
    model = Employee
    template_name = "tables.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Employee.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query) |
            Q(phone_number__icontains=query) | Q(age__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context



class ChartView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs"] = Employee.objects.values('city').annotate(city_count=Count('city')).order_by('-city_count')
        context["qs"] = Employee.objects.values('city')
        return context

