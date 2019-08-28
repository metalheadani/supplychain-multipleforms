from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import SimpleOrderForm, PurchaseOrderForm, QuotationForm, InvoiceForm

def multiple_forms(requset):
	template_name = 'varforms/home.html'
	
	if requset.method == 'POST':
		simpleorderform = SimpleOrderForm(requset.POST, prefix='simpleorder')
		if simpleorderform.is_valid():
			print('simpleorderform')
			print(simpleorderform)
			simpleorderform.save()
		else:
			return HttpResponse("Not valid")
	else:
		simpleorderform = SimpleOrderForm(prefix='simpleorder')

	if requset.method == 'POST' and not simpleorderform.is_valid():
		purchaseorderform = PurchaseOrderForm(requset.POST, prefix='purchaseorder')
		simpleorderform = SimpleOrderForm(prefix='simpleorder')
		if purchaseorderform.is_valid():
			print('simpleorderform')
			purchaseorderform.save()
		else:
			return HttpResponse("Not valid")
	else:
		purchaseorderform = PurchaseOrderForm(prefix='purchaseorder')

	if requset.method == 'POST' and not simpleorderform.is_valid() and not purchaseorderform.is_valid():
		quotationform = QuotationForm(requset.POST, prefix='quotation')
		simpleorderform = SimpleOrderForm(prefix='simpleorder')
		purchaseorderform = PurchaseOrderForm(prefix='purchaseorder')
		if quotationform.is_valid():
			print('simpleorderform')
			quotationform.save()
		else:
			return HttpResponse("Not valid")
	else:
		quotationform = QuotationForm(prefix='quotation')

	if requset.method == 'POST' and not simpleorderform.is_valid() and not purchaseorderform.is_valid() and not quotationform.is_valid():
		invoiceform = InvoiceForm(requset.POST, prefix='invoice')
		simpleorderform = SimpleOrderForm(prefix='simpleorder')
		purchaseorderform = PurchaseOrderForm(prefix='purchaseorder')
		quotationform = QuotationForm(prefix='quotation')
		if invoiceform.is_valid():
			print('simpleorderform')
			invoiceform.save()
		else:
			return HttpResponse("Not valid")
	else:
		invoiceform = InvoiceForm(prefix='invoice')

	context = {
	'simpleorderform':simpleorderform,
	'purchaseorderform':purchaseorderform,
	'quotationform':quotationform,
	'invoiceform':invoiceform,
	}
	return render(requset, template_name, context)
