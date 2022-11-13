from django import forms
from tab.models import Machine,Farmer,ServiceProvider

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name','gps_loc','description','barcode']
    
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        exclude = ('created',)
    

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        exclude = ('created',)
    
