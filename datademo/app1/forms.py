from django.forms import ModelForm
from app1.models import product

class ProductForm(ModelForm):
	class Meta(object):
		model=product
		fields=["prod_id","prod_name","price"]
