from django.db import models
#import datetime
#from django.utils import timezone
# Create your models here.
class Login_details(models.Model):
	Enter_Username =   models.CharField(max_length=30)
	Enter_Password =   models.CharField(max_length=50, null=True,blank=True)
	#pub_date = models.DateTimeField('Date Published',default=True)
	def __str__(self):
		return str((self.Enter_Username,self.Enter_Password))

'''
blank is used when we want that field may be taken as empty or filled
i.e., after using attribute as blank=true it is not necessary that we have to filled that field
we can also leave that field if we want.....
'''