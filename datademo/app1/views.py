from django.shortcuts import render
from app1.models import product
from app1.forms import ProductForm
# Create your views here.
def index(Request):
	data=product.objects.all()
	dic1={
		'data':data
	}
	return render(Request,"app1/index.html",dic1)

def addProduct(Request):
	form=ProductForm()
	dict1={
		'form':form
	}
	return render(Request,"app1/new_product.html",dict1)

def performAdd(Request):
	form=ProductForm()
	pid=Request.POST.get('prod_id')
	name=Request.POST.get('prod_name')
	price=Request.POST.get('price')

	product.objects.create(prod_id=pid,prod_name=name,price=price)
	data=product.objects.all()
	dict1={
		'form':form,
		'data':data
	}
	return render(Request,"app1/index.html",dict1)

def Edit(Request):
	id1=Request.GET.get('pid')
	data1=product.objects.get(prod_id=id1)
	dict1={
		'id':data1.prod_id,
		'name':data1.prod_name,
		'price':data1.price
	}
	return render(Request,"app1/edit_product.html",dict1)

def edit_action(Request):
	pid=Request.POST.get('pid')
	name=Request.POST.get('pname')
	price=Request.POST.get('pprice')
	obj=product.objects.filter(prod_id=pid).update(prod_name=name,price=price)
	data=product.objects.all()
	return render(Request,"app1/index.html",{'data':data})

def Delete(Request):
	id=Request.GET.get('pid')
	d=product.objects.get(prod_id=id)
	d.delete()
	data=product.objects.all()
	return render(Request,"app1/index.html",{'data':data})

