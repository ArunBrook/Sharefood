from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from app1.models import categoryA
from front1.models import regdb, product, sam
from .forms import DoctorSearchForm


# Crteate your views here.
# ------------samplepages------------
def sample_2(request):
    data = regdb.objects.all()
    return render(request, "sample_category", {'data': data})


def sample_3(request):
    data = regdb.objects.all()
    return render(request, "sample_3.html", {'data': data})


# ------------samplepages------------


def home(request):
    data = regdb.objects.all()
    beta = categoryA.objects.all()
    theta = product.objects.all()

    if request.method == 'GET':
        form = DoctorSearchForm(request.GET)
        doctors = []
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            if search_query:
                doctors = product.objects.filter(
                    P_name=search_query)
        return render(request, "F_home.html",
                      {'form': form, 'data': data, 'beta': beta, 'theta': theta, 'doctors': doctors})


def sample(request):
    data = regdb.objects.all()
    return render(request, "sample pages.html", {'data': data})


# --------------------------------------------------------------->register and login starts

def register(request):
    return render(request, "register.html")


def registersave(req):
    if req.method == "POST":
        un = req.POST.get('username')
        en = req.POST.get('email')
        mob = req.POST.get('mobile')
        ps = req.POST.get('password')
        img = req.FILES['image']
        obj = regdb(Username=un, mobile=mob, Email=en, Password=ps, Image=img)
        obj.save()
        return redirect(login)


def login(request):
    return render(request, "login.html")


def userlogin(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if regdb.objects.filter(Username=user, Password=pwd).exists():
            request.session['username'] = user
            request.session['password'] = pwd
            return redirect(home)
        else:
            return redirect(login)
    else:
        return redirect(login)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(home)


# ---------------------------------------------------------------> register and login ends----add food starts------------------------

def addfood(request):
    data = categoryA.objects.all()
    return render(request, "addfood.html", {'data': data})


def itemsave(req):
    if req.method == "POST":
        ca = req.POST.get('category')
        na = req.POST.get('item_name')
        qy = req.POST.get('quantity')
        mb = req.POST.get('mobile')
        lc = req.POST.get('Location')
        pr = req.POST.get('price')
        de = req.POST.get('description')
        sd = req.POST.get('sdescription')
        ll = req.POST.get('local')
        nm = req.POST.get('spopname')
        un = req.POST.get('uname')
        img1 = req.FILES['image1']
        img2 = req.FILES['image2']
        img3 = req.FILES['image3']
        obj = product(P_cata=ca, username=un, P_name=na, P_quantity=qy, P_number=mb, P_location=lc, P_price=pr,
                      P_sdescription=sd, P_description=de, P_image1=img1, P_image2=img2, P_image3=img3, P_localarea=ll,
                      P_shopname=nm)
        obj.save()
        return redirect(addfood)





def singleproduct(request, proid):
    catt = product.objects.get(id=proid)
    return render(request, "single.html", {'catt': catt, })


def pro(req, cat_name):
    data = categoryA.objects.all()
    catt = product.objects.filter(P_cata=cat_name)
    return render(req, "pro_cata.html", {'catt': catt, 'data': data})

def useradds(request):
    ss = product.objects.filter(username=request.session['username'])
    return render(request, 'view user product.html', {'ss': ss})




def productdeletee(req, proid):
    data = product.objects.filter(id=proid)
    data.delete()
    messages.warning(req, "Delete successfully")
    return redirect(useradds)


def editp(request, dataid):
    data = categoryA.objects.all()
    catt = product.objects.get(id=dataid)
    return render(request, "edit_product.html", {'catt': catt, 'data': data})

def categoryupdatee(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        na = request.POST.get('item_name')
        qy = request.POST.get('quantity')
        mb = request.POST.get('mobile')
        lc = request.POST.get('Location')
        pr = request.POST.get('price')
        de = request.POST.get('description')
        sd = request.POST.get('sdescription')
        ll = request.POST.get('local')
        nm = request.POST.get('spopname')
        try:
            img1 = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file = product.objects.get(id=dataid).P_image1
        try:
            img2 = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = product.objects.get(id=dataid).P_image2
        try:
            img3 = request.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file3 = product.objects.get(id=dataid).P_image3
        product.objects.filter(id=dataid).update(P_cata=ca, P_name=na, P_quantity=qy, P_number=mb, P_location=lc,
                                                   P_price=pr,
                                                   P_sdescription=sd, P_description=de, P_localarea=ll,
                                                   P_shopname=nm, P_image1=file , P_image2=file2 ,P_image3=file3)
        messages.success(request, "Update  Successfully")
        return redirect(useradds)



