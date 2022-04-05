from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from InventoryAssignment import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
]
urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
