

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render
from .views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return render(request, 'index.html')  #this renders the html

urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Include task app routes under /api/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
