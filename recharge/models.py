from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Mobile_recharge(models.Model):
	Enter_Your_Mobile_Number = models.CharField(max_length=10)
	TYPE = (
		('Postpaid', 'Postpaid'),
		('Prepaid', 'Prepaid'),
	)
	Recharge_Type = models.CharField(max_length=50, choices=TYPE)
	OPERATOR =(
		('Airtel', 'Airtel'),
		('Vodafone', 'Vodafone'),
		('Jio', 'Jio'),
		('Idea', 'Idea'),
		('Bsnl', 'Bsnl'),
		('Uninor', 'Uninor'),
	)
	Operator = models.CharField(max_length=50, choices=OPERATOR)
	CIRCLE =(
		('Andhra Pradesh', 'Andhra Pradesh'),
		('Assam', 'Assam'),
		('Bihar', 'Bihar'),
		('Haryana', 'Haryana'),
		('Delhi', 'Delhi'),
		('Gujarat', 'Gujarat'),
		('Uttar Pradesh', 'Uttar Pradesh'),
		('Himachal Pradesh', 'Himachal Pradesh'),
		('Karnataka', 'Karnataka'),
		('Madhya Pradesh', 'Madhya Pradesh'),
		('Mumbai', 'Mumbai'),
		('Chennai', 'Chennai'),
		('Tamil Nadu', 'Tamil Nadu'),
	)
	Circle = models.CharField(max_length=25, choices=CIRCLE)
	Recharge_Amount =models.IntegerField(default=10)
	Time_of_Recharge =models.DateTimeField()
	Currentuser = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
  	#Working of on_delete is that when certain User is deleted it also deleted the respective Mobile_recharge model associated with it.
	def __str__(self):
		return str((self.Enter_Your_Mobile_Number,self.Recharge_Type,self.Operator,self.Circle,self.Recharge_Amount,self.Currentuser))
	def pretty_time(self):
		return self.Time_of_Recharge.strftime('%b %e %Y')
	class Meta:
		ordering =['-id'] # This is used for showing the latest created model in the top of any template page where u want to show your models objects, basically tha latest object created is on the top of the template.


'''choices¶
Field.choices¶
An iterable (e.g., a list or tuple) consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field. If choices are given, they’re enforced by model validation and the default form widget will be a select box with these choices instead of the standard text field.

The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. For example:'''			

class Dth_recharge(models.Model):
	DTH =(
		('Dish TV', 'Dish TV'),
		('Videocon', 'Videocon'),
		('Tata Sky', 'Tata Sky'),
		('Airtel Tv', 'Airtel Tv'),
		('Sun Direct', 'Sun Direct'),
	)
	Select_DTH_Operator =models.CharField(max_length=50,choices=DTH)
	Customer_id =models.CharField(default=0,max_length=25)
	Recharge_Amount = models.IntegerField(default=0,blank=False,null=False)
	Currentuser = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	def __str__(self):
		return str((self.Select_DTH_Operator,self.Customer_id,self.Recharge_Amount,self.Currentuser))



class Metro_recharge(models.Model):
	TYPE = (
		('Delhi Metro', 'Delhi Metro'),
		('Hyderabad Metro', 'Hyder Metro'),
		('Mumbai Metro', 'Mumbai Metro'),
	)
	Select_Metro_Type =models.CharField(max_length=25,choices=TYPE)
	Card_Number =models.CharField(max_length=25)
	Recharge_Amount =models.IntegerField(blank=False,null=False)
	Currentuser = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	def __str__(self):
		return str((self.Select_Metro_Type,self.Card_Number,self.Recharge_Amount,self.Currentuser))

class Datacard_recharge(models.Model):
	Data_Card_Number =models.CharField(max_length=15)
	OPERATOR =(
		('Airtel', 'Airtel'),
		('Bsnl', 'Bsnl'),
		('Idea', 'Idea'),
		('Jio', 'Jio'),
		('MTNL', 'MTNL'),
		('Vodafone', 'Vodafone')
	)
	Select_Datacard_Operator =models.CharField(max_length=25,choices=OPERATOR)
	Recharge_Amount =models.IntegerField(blank=False,null=False)
	Currentuser = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	def __str__(self):
		return str((self.Data_Card_Number,self.Select_Datacard_Operator,self.Recharge_Amount,self.Currentuser))
		






