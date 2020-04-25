from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from django.db.models import Count
from django.shortcuts import *
from .forms import *

# Create your views here.
def index(request):
    store_all = Store.objects.all()

    cost = Store.objects.annotate(Count('cost'))
    cost = cost.values_list('store_id', 'cost__count')

    return render(request, 'content.html', {
        'stores': store_all,
        'cost': cost
    })

def aperture(request):
    if request.user.has_perm('management.change_aperture'):
        aperture_all = Aperture.objects.all()
    else:
        aperture_all = Aperture.objects.filter(aper_status=False)
    return render(request, 'view_aperture.html', {
        'apertures': aperture_all
    })

def my_login(request):
    context = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # --------------- เช็คว่า username, password มีอยู่ในข้อมูลหรือไม่ ----------------
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # next_url = request.POST.get('next_url')
            # if next_url:
            #     return redirect(next_url)
            # else:
            return redirect('index')
        else: # ไม่มีอยู่ในข้อมูล
            context = {
                'username': username,
                'password': password,
                'error': "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้องกรุณากรอกอีกครั้ง",
                'login_page': "login_page"
            }
            return render(request, 'login.html', context)
        # -------------------------------------------------------------------------
        

    # # -------- เมื่อมีการส่ง request next มา ----------
    # next_url = request.GET.get('next')
    # if next_url:
    #     context['next_url'] = next_url
    # # --------------------------------------------

    return render(request, 'login.html', context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('login')

def my_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            user = None

        if user or (password_1 != password_2):
            error = list()
            if user:
                error.append("กรุณาตั้ง username ใหม่")
            if password_1 != password_2:
                error.append("กรุณากรอกรหัสผ่านให้ตรงกัน")
            context = {
                'username': username,
                'password1': password_1,
                'password2': password_2,
                'errors': error
            }
            return render(request, 'register.html', context)
        else:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1')
            )
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            user.save()
            company = Company(
                company_name=request.POST.get('company_name'),
                company_address=request.POST.get('company_address'),
                company_phone=request.POST.get('company_phone'),
                contract_fname=request.POST.get('contract_fname'),
                contract_lname=request.POST.get('contract_lname'),
                other_notes=request.POST.get('other_notes'),
                account_acc_id_id=user.id,
            )
            company.save()
            return redirect('login')

    return render(request, 'register.html')

def store_detail(request, store_id):
    store = Store.objects.get(pk=store_id)
    return render(request, 'store.html', {
        'store': store
    })

def aperture_detail(request, aperture_id):
    aperture = Aperture.objects.get(pk=aperture_id)
    return render(request, 'aperture.html', {
        'aperture': aperture
    })

def add_manager(request, aperture_id):
    aperture = Aperture.objects.get(pk=aperture_id)
    if request.method == 'POST':
        manager = Manager(
            manag_fname=request.POST.get('manag_fname'),
            manag_lname=request.POST.get('manag_lname'),
            manag_level=request.POST.get('manag_level'),
            manag_phone=request.POST.get('manag_phone')
        )
        manager.save()
        aperture.aper_status = True
        aperture.save()
        return redirect('index')

    return render(request, 'manager.html', {
        'aperture_id': aperture_id
    })

def edit_store(request, store_id):
    store = Store.objects.get(pk=store_id)
    if request.method == 'POST':
        store.store_name = request.POST.get('store_name')
        store.phone = request.POST.get('phone')
        store.store_id = request.POST.get('store_id')
        store.branch = request.POST.get('branch')
        store.cost_total = request.POST.get('cost_total')
        store.manage_manag_id.manag_fname = request.POST.get('manag_fname')
        store.company_company_id.company_name = request.POST.get('company_name')
        store.repaired = request.POST.get('repaired')
        store.other_notes = request.POST.get('other_notes')
        store.save()
        return render(request, 'store_details.html', {
            'store': store
        })

    return render(request, 'edit_store.html', {
        'store': store
    })

def store_detail_edit(request, store_id):
    store = Store.objects.get(pk=store_id)
    return render(request, 'store_details.html', {
        'store': store
    })

def sale_view(request, aper_id):
    aper = Aperture.objects.get(pk=aper_id)
    return render(request, 'sale_view.html', {
        'aper': aper
    })

def add_store(request, aper_id):
    aper = Aperture.objects.get(pk=aper_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            aper.store_store_id_id = Store.objects.latest('store_id').store_id
            aper.save()
            return redirect('index')
    else:
        form = StoreForm()
    return render(request, 'add_store.html', {
        'form': form,
        'aper_id': aper_id
    })

def remove_store(request, store_id):
    if request.method == 'POST':
        store = Store.objects.get(pk=store_id)
        store.delete()
        return redirect('index')
        
    return render(request, 'question.html', {
        'store_id': store_id
    })

def edit_expenses(request, store_id):
    store = Store.objects.get(pk=store_id)
    aper = Aperture.objects.get(store_store_id=store_id)
    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CostForm()
    return render(request, 'edit_expenses.html', {
        'form': form,
        'store': store,
        'aper': aper
    })

def expenses_details(request, store_id):
    store = Store.objects.get(pk=store_id)
    aper = Aperture.objects.get(store_store_id=store_id)
    cost = Cost.objects.get(store_store_id=store_id)
    return render(request, 'add_expenses.html', {
        'store': store,
        'aper': aper,
        'cost': cost
    })
