from django.conf import settings
from django.shortcuts import redirect, render
from .forms import (MachineForm,FarmerForm,ServiceProviderForm)
from .models import Machine,ExcelFile
import pandas as pd
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
    machine_form = MachineForm(request.POST,request.POST,request.POST,request.POST)
    farmer_form = FarmerForm(request.POST,request.POST,request.POST)
    service_provider_form = ServiceProviderForm(request.POST,request.POST,request.POST)
    
    context = {
        'machine_form':machine_form,
        'farmer_form':farmer_form,
        'service_provider_form':service_provider_form,
        }
    return render(request,'home.html',context)



def excel_upload_view(request):
    # excel_file_name = request.FILES.get('file').name
    try:
        excel_file = request.FILES.get('file')
        # path = str(excel_file)
        # df = pd.read_excel(excel_file,sheet_name='Sheet1',header=2,usecols=['Person ID','Time','Attendance Status','Attendance Check Point','Custom Name','Data Source',])
        df = pd.read_excel(excel_file,sheet_name='Sheet1',header=2,usecols=['Person ID','Time','Attendance Status'])
        df['Time'] =pd.to_datetime(df['Time'])
        # df['Attendance Status'] =df['Attendance Status'].apply(lambda x: str(x))
        # df = pd.crosstab(df['Time'].dt.to_period('m'),df['Time'])
        # df['month']=df['Time'].dt.month
        # df['No Present'] = df.query('Attendance Status == "None"')
        # df.index=df['Time']
        
        pp=df.groupby(['Person ID',df['Time'].dt.month]).apply(lambda x: x[x['Attendance Status']=='None'].count())
        # df.groupby('Person ID',pd.Grouper(freq='M')).apply(lambda x:x)
        # ['price'].agg('sum')
        print(pp)
    except KeyError as w:
        print(w)

    # for value in df.values:
    #     data = value.tolist()
    #     print(data)

    return JsonResponse({
        'status':200
    })
   

'''
obj, created = ExcelFile.objects.get_or_create(file_name=excel_file_name)
if created:
    obj.excel_file = excel_file
    obj.save()
    path = str(excel_file)
    df = pd.read_excel(path)
    for value in df.values:
        data = value.tolist()
        name = ''.join(data[1])
        gps_loc = ''.join(data[2])
        description = ''.join(data[3])
        barcode = ''.join(data[4])
        Machine.objects.create(name=name,gps_loc=gps_loc,description=description,barcode=barcode)
        print( name,gps_loc,description,barcode)
return redirect('home')
'''
    
    

def machine_to_excel(request):
    objs = Machine.objects.all()
    data = []
    for obj in objs:
        data.append(
            {
              'name': obj.name,
              'gps location': obj.gps_loc,
              'description': obj.description,
              'barcode': obj.barcode,
              'added at': obj.created.strftime('%B %d, %Y'),
              'updated at': obj.updated.strftime('%B %d, %Y')
            }
        )
    pd1 = pd.DataFrame(data)
    print(pd1)
    pd1.to_excel("output2.xlsx",
              sheet_name='machine details') 
    return redirect('home')
    
