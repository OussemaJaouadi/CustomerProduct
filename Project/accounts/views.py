from .decorators import unauthenticated_user
from .forms import *
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'orders_delivered':orders_delivered,
        'orders_pending':orders_pending
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def Products_view(request):
    product_list = Product.objects.all()
    return render(request,'products.html',{
        'list' : product_list
    })

@login_required(login_url='login')
def Customer_view(request,id):
    customer = Customer.objects.get(pk=id)
    orders = customer.order_set.all()
    orders_total = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {
        'customer':customer,
        'orders':orders,
        'orders_total':orders_total,
        'myFilter':myFilter
    }
    return render(request,'customer.html',context)

@login_required(login_url='login')
def UOrder(request,order_id):
    if order_id==0 :
        print('Unautherised')
        redirect('/home')
    else :
        order = Order.objects.get(pk=order_id)
        form = OrderForm(instance=order)
        if request.method == 'POST':
            form =OrderForm(request.POST,instance=order)
            if form.is_valid :
                form.save()
                return redirect('/')
    context ={
        'form':form
    }
    return render(request,'order_update.html',context)

@login_required(login_url='login')
def COrder(request,customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3 )
    customer = Customer.objects.get(id=customer_id)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        else :
            print('invalid')
    context = {'formset':formset}
    return render(request, 'order_forum.html', context)

@login_required(login_url='login')
def DOrder(request,id):
    order = Order.objects.get(pk=id)
    if request.method =='POST':
        order.delete()
        return redirect('/')
    return render(request,'delete.html',{'order':order})

@unauthenticated_user
def Register(request):
    form = SignInForm()
    if request.method == 'POST':   
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully for '+user+' !' )
            return redirect('login')
    return render(request,'register.html',{
        'form':form
    })
    
@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password =password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else :
            messages.info(request,'Unvalid Data')

    return render(request,'login.html',{})

def Logout(request):
    logout(request=request)
    return redirect('/login')

def userPage(request):
    context = {}
    return render(request,'user.html',context)