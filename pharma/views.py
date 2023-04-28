from .models import Supplier
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from django.shortcuts import render
from django.db import IntegrityError


def home(request):
    return render(request, 'pharma/index.html')


def supplierform(request):
    return render(request, 'pharma/supplier.html', {'add': True})


def supplierforminsert(request):
    try:
        supplier = Supplier()
        supplier.sname = request.POST['sname']
        supplier.address = request.POST['address']
        supplier.phn_no = request.POST['pno']
        supplier.email = request.POST['email']
        supplier.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def supplierformupdate(request, foo):
    try:
        supplier = Supplier.objects.get(pk=foo)
        supplier.sname = request.POST['sname']
        supplier.address = request.POST['address']
        supplier.phn_no = request.POST['pno']
        supplier.email = request.POST['email']
        supplier.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def supplierformview(request, foo):
    supplier = Supplier.objects.get(pk=foo)
    return render(request, 'pharma/supplier.html', {'supplier': supplier})


def supplierformdelete(request, foo):
    supplier = Supplier.objects.get(pk=foo)
    supplier.delete()
    return render(request, 'pharma/index.html')


def suppliertable(request):
    supplier = Supplier.objects.all()
    return render(request, 'pharma/suppliertable.html',{'supplier':supplier})


def empform(request):
   return render(request, 'pharma/emp.html', {'add': True})


def empforminsert(request):
    try:
        emp = Employee()
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def empformupdate(request, foo):
    try:
        emp = Employee.objects.get(pk=foo)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def empformview(request, foo):
    emp = Employee.objects.get(pk=foo)
    return render(request, 'pharma/emp.html', {'emp':emp})


def empformdelete(request, foo):
    emp = Employee.objects.get(pk=foo)
    emp.delete()
    return render(request, 'pharma/index.html')


def emptable(request):
    emp = Employee.objects.all()
    return render(request, 'pharma/emptable.html', {"emp": emp})


def custform(request):
    return render(request, 'pharma/cust.html', {'add': True})


def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    return render(request, 'pharma/cust.html', {'cust': cust})


def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return render(request, 'pharma/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'pharma/custtable.html', dict)


def medform(request):
    return render(request, 'pharma/med.html', {'add':True})


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    return render(request, 'pharma/med.html', {'med': med})


def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return render(request, 'pharma/index.html')


def medtable(request):
    med = Medicine.objects.all()
    return render(request, 'pharma/medtable.html', {'med':med})


def purchaseform(request):
    return render(request, 'pharma/purchase.html', {'add':True})


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformupdate(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    return render(request, 'pharma/purchase.html', {'purchase': purchase})


def purchaseformdelete(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    purchase.delete()
    return render(request, 'pharma/index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    return render(request, 'pharma/purchasetable.html', {"purchase": purchase})
