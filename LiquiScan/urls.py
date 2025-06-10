from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import (
    AdministradorViewSet,
    BarraViewSet,
    CategoríaViewSet,
    AlcoholViewSet,
    CarouselItemViewSet,
    ListaDeAlcoholViewSet,
    ReporteViewSet,
    HelloWorldAPI,
    root_view,
)

router = routers.DefaultRouter()
router.register(r'administradores', AdministradorViewSet)
router.register(r'barras', BarraViewSet)
router.register(r'categorias', CategoríaViewSet)
router.register(r'alcoholes', AlcoholViewSet)
router.register(r'carousel-items', CarouselItemViewSet)
router.register(r'listas-de-alcohol', ListaDeAlcoholViewSet)
router.register(r'reportes', ReporteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view),
    path('api/', include(router.urls)),
    path('api/hello/', HelloWorldAPI.as_view(), name='api-hello'),
]
