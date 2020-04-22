from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import *
from .forms import *

# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     form = StoreForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = StoreForm()
    # return render(request, 'uplond_img.html', {
    #     'form': form
    # })

    store_all = Store.objects.all()
    return render(request, 'content.html', {
        'stores': store_all
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