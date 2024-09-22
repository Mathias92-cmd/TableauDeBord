from django.shortcuts import render , HttpResponse

from DashboardDevise import api


# Create your views here.

def dashboard(request, days_range=60 , currencies="USD"):
    days , rates = api.get_rates(currencies=currencies.split(",") , days=days_range)
    page_label = {7: "Semaine" , 30: "Mois" , 365: "Année"}.get(days_range , "Personnalisé")

    return render(request, "devise/index.html" , context={"data": rates ,
                                                                        "days_labels": days ,
                                                                        "currencies": currencies,
                                                                        "page_label": page_label})
