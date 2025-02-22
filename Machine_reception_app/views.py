from django.shortcuts import render
from .models import Mahcine_reception
from .forms import Machine_Search_Form
from django.http import JsonResponse

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

            
    
    context={'machine':queryset}
    
#     print(context['machine'])
    
    return render(request,'machine_reception.html', context=context)
