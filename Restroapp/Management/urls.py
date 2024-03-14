

from django.urls import path, include
from rest_framework import routers

from .views import CustomerViewSet, loginView, EmployeeViewSet, DashboardViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register('customer/', CustomerViewSet, basename='customers')
router.register('employee/', EmployeeViewSet, basename='employees')
router.register('dashboard/', DashboardViewSet, basename='dashboard')
# router.register('oldemployee/', OldEmployeeViewSet, basename='oldemployees')
urlpatterns = [
    path("", include(router.urls)),
    path("login/", loginView.as_view(), name="login"),
    
]