from django.db.models import Q
from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from inventory.models import Inventory
from inventory.serializer import InventorySerializer


class ChangeFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_list = list()
        if request.query_params.get('name'):
            filter_list.append(Q(name__in=request.query_params.getlist('name')))
        return queryset.filter(*filter_list)


class InventoryViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = Inventory.objects.all()
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]
    serializer_class = InventorySerializer
    filter_backends = [ChangeFilter]


def inventory(request):
    queryset = InventoryViewSet.as_view({'get': 'list'})(request)
    filter_data = [{'name': data.get('name'),
                    'availability': data.get('availability'),
                    'supplier_name': data.get('supplier').get('name')}
                   for data
                   in queryset.data]
    context = {'all_inventories': filter_data}

    return render(request, 'inventory.html', context)


def inventory_single(request, pk):
    queryset = Inventory.objects.filter(pk=pk).values().first()
    context = {'data': queryset}
    return render(request, 'inventory_single.html', context)
