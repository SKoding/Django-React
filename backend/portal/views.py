from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_gis import filters
from .models import farm, farmer, partner
from .serializer import farmSerializer, farmerSerializer, partnerSerializer
from django.db.models import Q
from rest_framework import generics 
from rest_framework import filters as restFilter


class farmViewSet(viewsets.ModelViewSet):

    bbox_filter_field = "geom"
    filter_backends = (filters.InBBOXFilter,)
    queryset = farm.objects.all() #manager that returns queryset object same as SELECT * ALL FROM farms
    serializer_class = farmSerializer
    bbox_filter_include_overlapping = True

class farmerViewSet(viewsets.ModelViewSet):
    queryset = farmer.objects.all()
    serializer_class = farmerSerializer

class partnerViewSet(viewsets.ModelViewSet):
    queryset = partner.objects.all()
    serializer_class = partnerSerializer

class SearchPost(generics.ListAPIView):
    model = farmer
    serializer_class = farmSerializer
    filter_backends = [restFilter.SearchFilter]
    def get_queryset(request):    
        query = request.GET.get("q")  
        if query:
            searchQ = farmer.objects.filter(
                Q(farmID_icontains=query)).distinct()
        else:
            searchQ = []
        return searchQ  




