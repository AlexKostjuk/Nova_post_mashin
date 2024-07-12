from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from parcel import models

# Create your views here.
def parcels_view(requst):
    return HttpResponse("helo start meni")


def one_parcel_view(requst, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)
    return HttpResponse(f"helo start one {parcel_id}")

