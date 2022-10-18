from django.shortcuts import render
from .forms import (MachineForm,FarmerForm,ServiceProviderForm)
# Create your views here.
def home(request):
    machine_form = MachineForm(request.POST,request.POST,request.POST,request.POST)
    farmer_form = FarmerForm(request.POST,request.POST,request.POST)
    service_provider_form = ServiceProviderForm(request.POST,request.POST,request.POST)
    context = {
        'machine_form':machine_form,
        'farmer_form':farmer_form,
        'service_provider_form':service_provider_form,
        }
    return render(request,'home.html',context)


