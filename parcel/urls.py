from django.contrib import admin
from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcels_view),
    path('<parcel_id>/', parcel.views.one_parcel_view),

]
