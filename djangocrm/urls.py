from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet) # this creates the url for view itself
router.register(r'products', views.ProductViewSet) # this creates the url for view itself

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include("webapp.urls")),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
