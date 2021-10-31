from django.db import models
# Create your models here.
class Register_details(models.Model):
	Enter_Name           = models.CharField(max_length=50)  #max length=required length
	Enter_Email_address  = models.EmailField(max_length=30)
	Enter_Username       = models.CharField(max_length=30)
	Enter_Phone    		 = models.IntegerField(default=0)
	Enter_Password       = models.CharField(max_length=32)
	def __str__(self):
		return str((self.Enter_Name,self.Enter_Email_address,self.Enter_Username,self.Enter_Phone,self.Enter_Password))



 
