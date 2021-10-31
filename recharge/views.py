from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mobile_recharge
from .models import Dth_recharge
from .models import Datacard_recharge
from .models import Metro_recharge
from django.utils import timezone
from django.http import HttpResponse 
# Create your views here.
@login_required
def mobile(request):
	if request.method == 'POST':
		if request.POST['mobilenumber'] and request.POST['type'] and request.POST['operator'] and request.POST['circle'] and request.POST['amount']:
			mobile = Mobile_recharge()  #here created the object of the class to access their features
			mobile.Enter_Your_Mobile_Number =request.POST['mobilenumber']
			mobile.Recharge_Type =request.POST['type']
			mobile.Operator=request.POST['operator']
			mobile.Circle =request.POST['circle']
			mobile.Recharge_Amount =request.POST['amount']
			mobile.Time_of_Recharge =timezone.datetime.now()
			mobile.Currentuser =request.user
			mobile.save()

			return redirect('paymentindex')
		else:
			return render(request,'recharge/mobile.html',{'warning':'All Fields Must be Filled.'})

	else:
		return render(request,'recharge/mobile.html')


@login_required
def dth(request):
	if request.method == 'POST':
		if request.POST['type'] and request.POST['id'] and request.POST['Amount']:
			dth = Dth_recharge()
			dth.Select_DTH_Operator =request.POST['type']
			dth.Customer_id =request.POST['id']
			dth.Recharge_Amount=request.POST['Amount']
			dth.Currentuser =request.user

			dth.save()
			return redirect('paymentindex')
		else:
			return render(request,'recharge/dth.html',{'warning':'All Fields Must be Filled.'})

	else:
		return render(request,'recharge/dth.html')	
		

@login_required
def datacard(request):
	if request.method =='POST':
		if request.POST['datacard'] and request.POST['type'] and request.POST['Amount']:
			datacard = Datacard_recharge()
			datacard.Data_Card_Number =request.POST['datacard']
			datacard.Select_Datacard_Operator =request.POST['type']
			datacard.Recharge_Amount =request.POST['Amount']
			datacard.Currentuser=request.user
			datacard.save()
			return redirect('paymentindex')
		else:
			return render(request,'recharge/datacard.html',{'warning':'All Fields Must be Filled'})
	else:
		return render(request,'recharge/datacard.html')
	
@login_required
def metro(request):
	if request.method =='POST':
		if request.POST['type'] and request.POST['number'] and request.POST['Amount']:
			metro = Metro_recharge()
			metro.Select_Metro_Type =request.POST['type']
			metro.Card_Number =request.POST['number']
			metro.Recharge_Amount =request.POST['Amount']
			metro.Currentuser =request.user
			metro.save()
			return redirect('paymentindex')
		else:
			return render(request,'recharge/metro.html',{'warning':"All Fields Must be Filled"})
	else:
		return render(request,'recharge/metro.html')

@login_required
def payment(request):
	if request.method =='POST':
		if request.POST['noc'] and request.POST['cno'] and request.POST['exp'] and request.POST['cvv']:
			return redirect('successindex')
		else:
			return render(request,'recharge/payment.html',{'warning':"All Fields Must be Filled"})

	else:
		return render(request,'recharge/payment.html')

@login_required
def success(request):
	return render(request,'recharge/success.html')

#TODO We Want to show the History of a particular User.
'''def mobilerid(request,recharge_id):
	history =get_object_or_404(Mobile_recharge,pk=recharge_id)
	return render(request,'recharge/history.html',{'history':history})'''

'''
###############################TO SHOW THE DATABASAE ON THE HTML PAGE##############################################

def show(request):
	var =Modelname/classname.objects.all()
	return render(request,'appname/showpage.html',{"key":var})


'''
