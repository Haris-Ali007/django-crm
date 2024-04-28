from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Product, Purchase

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label=''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label=''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmation password'
        self.fields['password2'].label=''

    
class CustomerRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    phone_number = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    address = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))

    class Meta:
        model = Customer
        exclude = ('id',)


class ProductInfoForm(forms.ModelForm):
    product_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}))
    
    class Meta:
        model = Product
        exclude = ('id',)


class PurchaseInfoForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        exclude = ('id',)

# class PurchaseInfoForm(forms.ModelForm):
#     customers = Customer.objects.values_list('id', 'first_name', 'last_name')
#     customers = list(map(lambda x: (x[0], f"{x[1]} {x[2]}"), customers))
#     products = Product.objects.values_list('id', 'product_name')
#     customer_id = forms.ChoiceField(label="Customer", choices=customers, required=True, widget=forms.Select(attrs={'class':'form-control'}))
#     product_id = forms.ChoiceField(label="Product", choices=products, required=True, widget=forms.Select(attrs={'class':'form-control'}))

#     class Meta:
#         model = Purchase
#         fields = ['customer_id', 'product_id', 'quantity']
