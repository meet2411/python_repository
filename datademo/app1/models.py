from django.db import models

# Create your models here.
class product(models.Model):
	prod_id=models.CharField(max_length=50)
	prod_name=models.CharField(max_length=50)
	price=models.CharField(max_length=50)

	def __str__(self):
		return self.prod_id+" "+self.prod_name+" "+self.price
