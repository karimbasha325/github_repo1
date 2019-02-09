from django.shortcuts import render
from testApp.models import Hydjobs,Chennaijobs,Blorejobs,Kochijobs

# Create your views here.
def Index(request):
    return render(request,'testApp/index.html')

def hydjobs(request):
    jobs_list=Hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/hyd.html',context=my_dict)

def chennaijobs(request):
    jobs_list=Chennaijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/chennai.html',context=my_dict)

def blorejobs(request):
    jobs_list=Blorejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/blore.html',context=my_dict)

def kochijobs(request):
    jobs_list=Kochijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/kochi.html',context=my_dict)
