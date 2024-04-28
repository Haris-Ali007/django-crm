from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, CustomerRecordForm, ProductInfoForm, PurchaseInfoForm
from .models import Customer, Product, Purchase

def index(request):
    records = Customer.objects.all().order_by('id')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message='Logged in successfully...')
            return redirect('index')
        else:
            messages.warning(request, message='Error logging in user')
            return redirect('index')
    else:
        return render(request, 'index.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, message="Logged out successfully")
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, message='You have successfully registered')
            return redirect('index')
        # else:
        #     messages.warning(request, message='Registeration failed')
        #     return redirect(request, 'register')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        form = SignUpForm()
    return render(request, 'register.html', {"form":form})

@login_required(login_url='/webapp/')
def product_records(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'products.html', {'products':products})

@login_required(login_url='/webapp/')
def purchase_records(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases.html', {'purchases':purchases})

@login_required(login_url='/webapp/')
def update_customer(request, cid):
    customer_record = Customer.objects.get(id=cid)
    form = CustomerRecordForm(request.POST or None, instance=customer_record)
    if form.is_valid():
        form.save()
        messages.success(request, message='Records updated successfully')
        return redirect('index')
    return render(request, 'update_customer.html', {'form':form, 'customer_id': cid})

@login_required(login_url='/webapp/')
def delete_customer(request, cid):
    customer_record = Customer.objects.get(id=cid)
    customer_record.delete()
    messages.success(request, message='Record deleted successfully')
    return redirect('index')

@login_required(login_url='/webapp/')
def add_customer(request):
    if request.method=="POST":
        form = CustomerRecordForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, message="New record added")
            return redirect('index')
    else:
        form = CustomerRecordForm()
    return render(request, 'add_customer.html', {'form':form})

@login_required(login_url='/webapp/')
def add_product(request):
    if request.method=="POST":
        form = ProductInfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, message="New product added")
            return redirect('products')
    else:
        form = ProductInfoForm()
    return render(request, 'add_products.html', {'form':form})

@login_required(login_url='/webapp/')
def update_product(request, pid):
    product_record = Product.objects.get(id=pid)
    form = ProductInfoForm(request.POST or None, instance=product_record)
    if form.is_valid():
        form.save()
        messages.success(request, message='Product info updated successfully')
        return redirect('products')
    return render(request, 'update_product.html', {'form':form, 'product_id':pid})

@login_required(login_url='/webapp/')
def delete_product(request, pid):
    product_record = Product.objects.get(id=pid)
    product_record.delete()
    messages.success(request, message='Record deleted successfully')
    return redirect('products')

@login_required(login_url='/webapp/')
def add_purchases(request):
    if request.method=="POST":
        form = PurchaseInfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            # update inventory detail as well
            purchased_quantity = form.data["quantity"]
            product_id = form.data["product_id"]
            product_info = Product.objects.get(id=product_id)
            current_quantity = product_info.inventory_left
            product_info.inventory_left = int(current_quantity) - int(purchased_quantity)
            product_info.save()
            messages.success(request, message="New purchases record added")
            return redirect('purchases')
    else:
        form = PurchaseInfoForm()
    return render(request, 'add_purchases.html', {'form':form})

@login_required(login_url='/webapp/')
def delete_purchase(request, prid):
    purchase_record = Purchase.objects.get(id=prid)
    purchase_record.delete()
    messages.success(request, message='Record deleted successfully')
    return redirect('purchases')


