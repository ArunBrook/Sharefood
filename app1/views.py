from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from app1.models import categoryA

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def back_home(request):
    return render(request, "back_home.html")


def add_catacory(request):
    return render(request, "add_catacory.html")


def categorysave(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        dn = request.POST.get('description')
        img = request.FILES['image']
        obj = categoryA(A_categoryname=cn, A_description=dn, A_image=img)
        obj.save()
        # messages.success(req,"Category Save Successfully")
        return redirect(add_catacory)


def categorydisp(request):
    data = categoryA.objects.all()
    return render(request, "category display.html", {'data': data})


def categoryedit(request, dataid):
    data = categoryA.objects.get(id=dataid)
    return render(request, "edit_c.html", {'data': data})


def categoryupdate(request, dataid):
    if request.method == "POST":
        ct = request.POST.get("categoryname")
        ds = request.POST.get("description")
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categoryA.objects.get(id=dataid).A_image
        categoryA.objects.filter(id=dataid).update(A_categoryname=ct, A_description=ds, A_image=file)
        messages.success(request, "Update  Successfully")
        return redirect(categorydisp)


def categorydelete(req, dataid):
    data = categoryA.objects.filter(id=dataid)
    data.delete()
    messages.warning(req, "Delete Successfully")
    return redirect(categorydisp)


def staff_page(request):
    return render(request, 'staff_page.html')


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def staff_page(request):
    return render(request, 'staff_page.html')
