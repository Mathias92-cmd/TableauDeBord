from django.db.models.sql.compiler import cursor_iter
from django.shortcuts import render , redirect

from DashboardDevise import api


def custom_redirect(request):
    return redirect("dashboard" , days_range=30 , currencies="USD")

def dashboard(request, days_range=60 , currencies="USD"):
    days , rates = api.get_rates(currencies=currencies.split(",") , days=days_range)
    page_label = {7: "Semaine" , 30: "Mois" , 365: "Année"}.get(days_range , "Personnalisé")

    return render(request, "devise/index.html" , context={"data": rates ,
                                                                        "days_labels": days ,
                                                                        "currencies": currencies,
                                                                        "page_label": page_label})
