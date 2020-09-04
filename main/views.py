from django.shortcuts import render
from covid import Covid
# Create your views here.
def corona(request):
    cd = Covid(source="worldometers")
    
    if request.method =='POST':
        country=request.POST['country']
        
       
        content=cd.get_status_by_country_name(country)
        
        data={
            'country':str(content['country']),
            'confirmed':int(content['confirmed']),
            'active':str(content['active']),
            'deaths':str(content['deaths']),
            'recovered':str(content['recovered']),
            'new_cases':str(content['new_cases']),
        }
    else:
        data={}
       
        print('no daata')    
    
  
    return render(request,'index.html',data)
