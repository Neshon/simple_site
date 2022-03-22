from django.shortcuts import render
from django.views import generic

from advertisement.models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'
