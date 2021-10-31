from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Images(models.Model):
	job_image = models.ImageField(upload_to='save_images/')
	details   = models.CharField(max_length=300,null=True)  #max_length="300" is wrong so remove double quotes
	pub_date  = models.DateTimeField('Date Published')
	description_about_yourself =models.TextField(default="Describe in Brief")
	def __str__(self):
		return str((self.job_image,self.details,self.pub_date,self.description_about_yourself))
		
