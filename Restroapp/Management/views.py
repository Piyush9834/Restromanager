from django.shortcuts import render
from .models import User, Customer, Employee, OldEmployee
from rest_framework.decorators import action
from . import serializer
from dj_rest_kit.views import BaseAPIView, BaseUUIDViewSet
from django.contrib.auth import authenticate
from rest_framework import permissions, serializers, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class loginView(BaseAPIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user and not user.is_active:
            raise AuthenticationFailed("User is not active!")
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
            
            response.update(**serializer.UserLogineSerializer(user).data)
            return Response(response)
        else:
            raise AuthenticationFailed("Invalid email or password")
        
class CustomerViewSet(BaseUUIDViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializer.CustomerSerializer
   
    #added
    
    # @action(detail=True, methods=['Post'])
    # def print_slip(self, request, pk=None, *args, **kwargs):
    #     print(kwargs)
    #     print(args)
    #     queryset = self.get_object()
    #     print(queryset)
    #     name = queryset.first_name
    #     mobile = queryset.mobile
    #     item = queryset.purchesed_item
    #     total = queryset.total_price
    #     response = {
    #         'name': name,
    #         'item': item,
    #         'mobile': mobile,
    #         'total': total
    #     }
    
    #     return response
    
    
class EmployeeViewSet(BaseUUIDViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    
    
class OldEmployeeViewSet(BaseUUIDViewSet):
    queryset = OldEmployee.objects.all()
    serializer_class = serializer.OldEmployeeSerializer
    
class DashboardViewSet(BaseUUIDViewSet):
    def get(self, request):
        pass
        return render(request, 'dashboard.html')