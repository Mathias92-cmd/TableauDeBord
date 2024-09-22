from django.shortcuts import render , HttpResponse

from DashboardDevise import api


# Create your views here.

def dashboard(request):
    days , rates = api.get_rates(currencies=["USD"] , days=30)
    return render(request, "devise/index.html" , context={"data": rates["USD"] ,
                                                                        "days_labels": days})
