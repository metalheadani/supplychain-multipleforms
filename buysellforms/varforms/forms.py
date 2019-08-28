from django import forms
from django.utils import timezone


class SimpleOrderForm(forms.Form):
	uid = forms.CharField(label="UID", max_length=250)
	quantity = forms.IntegerField()
	description = forms.CharField(label="UID", max_length=250)
	item = forms.CharField(label="UID", max_length=150)


class PurchaseOrderForm(forms.Form):
	uid = forms.CharField(label="UID", max_length=250)
	orderuid = forms.CharField(label="Order UID", max_length=250)
	quantity = forms.IntegerField()
	cost = forms.IntegerField()
	timeofpurchase = forms.DateTimeField(label="Time of Purchase")
	timefordelivery = forms.DateTimeField(label="Time for Delivery")


class QuotationForm(forms.Form):
	uid = forms.CharField(label="UID", max_length=250)
	orderuid = forms.CharField(label="Order UID", max_length=250)
	quantity = forms.IntegerField()
	cost = forms.IntegerField()
	timefordelivery = forms.DateTimeField(label="Time for Delivery")
	seller = forms.CharField(label="UID", max_length=250)


class InvoiceForm(forms.Form):
	uid = forms.CharField(label="UID", max_length=250)
	buyer = forms.CharField(label="UID", max_length=250)
	finalamount = forms.IntegerField(label="Final Amount")
	seller = forms.CharField(label="UID", max_length=250)