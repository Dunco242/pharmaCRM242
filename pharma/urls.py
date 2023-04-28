from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

    path('supplierform/', views.supplierform, name="supplierform"),
    path('supplierforminsert/', views.supplierforminsert, name="supplierforminsert"),
    path('supplierformupdate<int:foo>/', views.supplierformupdate, name="supplierformupdate"),
    path('supplierformview<int:foo>/', views.supplierformview, name="supplierformview"),
    path('supplierformdelete<int:foo>/', views.supplierformdelete, name="supplierformdelete"),
    path('suppliertable/', views.suppliertable, name='suppliertable'),

    path('medform/', views.medform, name="medform"),
    path('medforminsert/', views.medforminsert, name="medforminsert"),
    path('medformupdate<int:foo>/', views.medformupdate, name="medformupdate"),
    path('medformview<int:foo>/', views.medformview, name="medformview"),
    path('medformdelete<int:foo>/', views.medformdelete, name="medformdelete"),
    path('medtable/', views.medtable, name='medtable'),

    path('empform/', views.empform, name="empform"),
    path('empforminsert/', views.empforminsert, name="empforminsert"),
    path('empformupdate<int:foo>/', views.empformupdate, name="empformupdate"),
    path('empformview<int:foo>/', views.empformview, name="empformview"),
    path('empformdelete<int:foo>/', views.empformdelete, name="empformdelete"),
    path('emptable/', views.emptable, name='emptable'),

    path('custform/', views.custform, name="custform"),
    path('custforminsert/', views.custforminsert, name="custforminsert"),
    path('custformupdate<int:foo>/', views.custformupdate, name="custformupdate"),
    path('custformview<int:foo>/', views.custformview, name="custformview"),
    path('custformdelete<int:foo>/', views.custformdelete, name="custformdelete"),
    path('custtable/', views.custtable, name='custtable'),

    path('purchaseform/', views.purchaseform, name="purchaseform"),
    path('purchaseforminsert/', views.purchaseforminsert, name="purchaseforminsert"),
    path('purchaseformupdate<int:foo>/', views.purchaseformupdate, name="purchaseformupdate"),
    path('purchaseformview<int:foo>/', views.purchaseformview, name="purchaseformview"),
    path('purchaseformdelete<int:foo>/', views.purchaseformdelete, name="purchaseformdelete"),
    path('purchasetable/', views.purchasetable, name='purchasetable')
]
