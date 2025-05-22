from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
    shipping_phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=True)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)
    shipping_pincode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pincode'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_phone', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_country', 'shipping_pincode']
        exclude = ['user',]

class PaymentForm(forms.Form):
    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name on Card'}), required=True)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Number'}), required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Expiry Date'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVV Number'}), required=True)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing Address 1'}), required=True)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing Address 2'}), required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing City'}), required=True)
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing State'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing Country'}), required=True)
    card_pincode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing Pincode'}), required=True)

    