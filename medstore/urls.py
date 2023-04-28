from django.urls import path, include
from django.contrib import admin
from pharma import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pharma/', include('pharma.urls')),
    path('', views.home, name='index'),
]
