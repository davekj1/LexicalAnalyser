from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def button(request):
	return render(request,'home.html')

	return render(request,'home.html',{'data':data})
def external(request):
	inp=request.POST.get('param')

	out=run([sys.executable,'C:\\Users\\Hp\\django\\test.py',inp],shell=False,stdout=PIPE)

	return render(request,'home.html',{'data1':out.stdout.decode("UTF-8"),'data2':inp})
