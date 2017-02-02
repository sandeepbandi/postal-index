from django.shortcuts import render
from django.db import models
from .models import postindtable
from django.shortcuts import render_to_response
from django.template import Context
from .form import UserForm
# Create your views here.
def import_db(request):
    
    f = open('/home/sandeep/Desktop/postalpro/newpostpro/nppapp/csv/all_india_pin_code.csv', 'r')  
    for line in f:
        line =  line.split(',')
        tmp = postindtable.objects.create()
        tmp.officename = line[0]
        tmp.pincode= line[1]
        tmp.officeType = line[2]
        tmp.Deliverystatus = line[3]
        tmp.divisionname = line[4]
        tmp.regionname = line[5]
        tmp.circlename = line[6]
        tmp.taluk = line[7]
        tmp.Districtname = line[8]
        tmp.statename = line[9]
    	tmp.save()

    f.close()
def home(request):
   return render(request,'nppapp/da.html')


def retrieve(request):
   if request.method == 'POST':
      form = UserForm(request.POST)
      print(form)
      if form.is_valid():
         PINCODE = request.POST.get('PINCODE')
         print(PINCODE)
         x = postindtable.objects.filter(pincode=PINCODE)
         print(x)
   return render_to_response("nppapp/data.html", {'x':x}, context_instance=Context(request))