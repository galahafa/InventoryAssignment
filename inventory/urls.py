from django.urls import path

from inventory.views import InventoryViewSet, inventory, inventory_single

urlpatterns = [
    path('api/inventory', InventoryViewSet.as_view({'get': 'list'})),
    path('inventory', inventory, name='inventory'),
    path('inventory/<int:pk>', inventory_single, name='one_inventory'),


]
