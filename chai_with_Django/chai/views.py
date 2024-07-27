from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_list_or_404
# Create your views here.
def all_chai(request):
    chai= ChaiVariety.objects.all()
    return render(request,"all_chai.html",{"chais":chai})

def chai_detail(request,chai_id):
    chai=get_list_or_404(ChaiVariety,pk=chai_id)
    return render(request,"chai_details.html",{"chai":chai})
    
    
