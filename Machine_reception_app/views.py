from django.shortcuts import render
from .models import Mahcine_reception
from .forms import Machine_Search_Form
from django.http import JsonResponse
import csv
from django.http import HttpResponse

# Create your views here.

def machine_reception(request):
    # form=Machine_Search_Form(request.POST or None)
   
    queryset=Mahcine_reception.objects.all()

 

    MN = request.POST.get('MN')
    MRC=request.POST.get('MRC')
  
  
    if request.method=="POST" :
            if MN:
                  queryset=Mahcine_reception.objects.filter( MN__icontains=MN ).values()
            if MRC:
                  queryset=Mahcine_reception.objects.filter( MRC__icontains=MRC ).values()
                  
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                  # If the request is AJAX, return JSON response
                  data = list(queryset.values('MN', 'MRC', 'technician_name', 'shelf'))
                  return JsonResponse({'machine': data})
            
            if request.POST.get('export_cvs')=='on':
                  response=HttpResponse(content_type='text/csv')
                  response['Content-Disposition']='attachment; filename="machine_reception.csv"'
                  writer=csv.writer(response)
                  writer.writerow(['Machine Number','Technicain Name','SHELF'])
                  # instance=queryset   
                  print('The quick grronw fos ',type(response))
                  for machine in queryset:# use instance variable to export entire datas
                        writer.writerow([machine.MRC,machine.technician_name,machine.shelf])
                  return response

            
            # print('The quick brown fox jumping over the lazy dog',request.POST.get('export_cvs'))
            # print(request.POST.get('export_cvs'))
            
           
    context={'machine':queryset}
    
#     print(context['machine'])
    
    return render(request,'machine_reception.html', context=context)
