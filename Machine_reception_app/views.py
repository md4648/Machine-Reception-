from django.shortcuts import render
from .models import Mahcine_reception
from .forms import Machine_Search_Form

# Create your views here.

def machine_reception(request):
    # form=Machine_Search_Form(request.POST or None)
   
    queryset=Mahcine_reception.objects.all()

 

    MN = request.POST.get('MN')
    MRC=request.POST.get('MRC')

  
    if request.method=="POST" :
            if MN:
                  queryset=Mahcine_reception.objects.filter( MN=MN )
            if MRC:
                  queryset=Mahcine_reception.objects.filter( MRC=MRC )
            
    
    context={'machine':queryset}
    
    print(context['machine'])
    
    return render(request,'machine_reception.html', context=context)
