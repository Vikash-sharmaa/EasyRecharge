from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Login_details
from django.contrib import auth
# Create your views here.
'''
def index(request):
	return HttpResponse("Hello this is login page")'''
################################TO SHOW CONTENT OF MODELS OR FIELDS OF MODEL ON THE HTML PAGE#################
'''def index(request):
	context={}
	context['data'] =Login_details.objects.all()
	return render(request,'login/index.html',context)'''
def index(request):
	if request.method =='POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
		if user is not None:
			auth.login(request,user)
			return redirect('homeindex')
			
		else:
			return render(request,'login/index.html',{'error':'username or password is incorrect '})

	else:
		return render(request,'login/index.html',{'error':'You need to Login First'})


def logout(request):
	if request.method =='POST':
		auth.logout(request)
		return redirect('homeindex')



#context['data'] is used when we want to show the data of models or corresponding app in the index.html of the 
#corresponding app	

#here None means we cannot get a valid user it means user is not find in their database, None simply says that they
#not found any valif user from the database of users


def guest(request):
	return render(request,'login/guest.html')