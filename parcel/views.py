from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from parcel import models

# Create your views here.
def parcels_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, 'parcels.html', context={'parcels':parcels})


def one_parcel_view(request, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)
    return render(request, 'one_parcel.html', context={'parcel': result})
