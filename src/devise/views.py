from django.shortcuts import render, redirect as django_redirect
from DashboardDevise import api

def custom_redirect(request):
    return django_redirect("dashboard_with_params", days_range=7, currencies="USD")

def dashboard(request, days_range=60, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "currencies": currencies,
                                                         "page_label": page_label})