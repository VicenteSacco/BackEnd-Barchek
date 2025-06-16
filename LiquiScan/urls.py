from django.urls import path
from myapp.views import AlcoholListCreate, AlcoholRetrieveUpdateDestroy,alcohol_list,alcohol_create,ReporteListCreate,ReporteRetrieveUpdateDestroy,AdministradorListCreate,AdministradorRetrieveUpdateDestroy,BarraListCreate,BarraRetrieveUpdateDestroy,ListaaalcoholRetrieveUpdateDestroy,ListaaalcoholListCreate,ListaDeAlcoholListCreate,ListaDeAlcoholRetrieveUpdateDestroy
from myapp.views import BartenderListCreate,BartenderRetrieveUpdateDestroy,EstimateLiquidView,RegenerarPinAdministrador,BuscarListasPorAdmin,BuscarAlcoholesPorLista,BuscarBarrasPorAdmin,BartendersPorAdministradorConBarra
from myapp import views
from django.contrib import admin
from myapp.views import login_view, register_view, dashboard_view
from rest_framework_simplejwt.views import TokenRefreshView
from myapp.auth import login, register, bartender_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alcohol_list/', views.alcohol_list, name='alcohol_list'),
    path('alcohol/create/', views.alcohol_create, name='alcohol_create'),
    path('alcohol/update/<int:pk>/', views.alcohol_update, name='alcohol_update'),
    path('alcohol/delete/<int:pk>/', views.alcohol_delete, name='alcohol_delete'),
  
    # API Endpoints genericos (GET,POST,PUT,PTACH,DELETE)
    path('api/alcohol/', AlcoholListCreate.as_view(), name='alcohol-list-create'),
    path('api/alcohol/<int:pk>/', AlcoholRetrieveUpdateDestroy.as_view(), name='alcohol-detail'),
    path('api/reportes/', views.ReporteListCreate.as_view(), name='reportes-list-create'),
    path('api/reportes/<int:pk>/', views.ReporteRetrieveUpdateDestroy.as_view(), name='reportes-detail'),
    path('api/administrador/', views.AdministradorListCreate.as_view(), name='administrador-list-create'),
    path('api/administrador/<int:pk>/', views.AdministradorRetrieveUpdateDestroy.as_view(), name='administrador-detail'),
    path('api/barra/', views.BarraListCreate.as_view(), name='barra-list-create'),
    path('api/barra/<int:pk>/', views.BarraRetrieveUpdateDestroy.as_view(), name='barra-detail'),
    path('api/Lista_a_alcohol/', views.ListaaalcoholListCreate.as_view(), name='Lista_a_alcohol-list-create'),
    path('api/Lista_a_alcohol/<int:pk>/', views.ListaaalcoholRetrieveUpdateDestroy.as_view(), name='Lista_a_alcohol-detail'),
    path('api/Lista_de_alcohol/', views.ListaDeAlcoholListCreate.as_view(), name='lista_de_alcohol-list-create'),
    path('api/Lista_de_alcohol/<int:pk>/', views.ListaDeAlcoholRetrieveUpdateDestroy.as_view(), name='lista_de_alcohol-detail'),
    path('api/Bartender/', views.BartenderListCreate.as_view(), name='Bartender-list-create'),
    path('api/Bartender/<int:pk>/',views.BartenderRetrieveUpdateDestroy.as_view(), name='Bartender-detail'),

    # Endpoints especificos (FILTROS)
    path('api/administrador/<int:pk>/regenerar_pin/', views.RegenerarPinAdministrador.as_view(), name='regenerar-pin'),
    path('api/Lista_de_alcohol/<int:pk>/filtrar_lista/', views.BuscarListasPorAdmin.as_view(), name='BuscarListasPorAdmin'),
    path('api/Lista_a_alcohol/<int:pk>/filtrar_lista/', views.BuscarAlcoholesPorLista.as_view(), name='BuscarListasIdLista'),
    path('api/barra/<int:pk>/filtrar_barra/', views.BuscarBarrasPorAdmin.as_view(), name='barra-por-idadmin'),
    path('api/bartenders_por_administrador_con_barra/<int:pk>/', BartendersPorAdministradorConBarra.as_view(), name='bartenders-por-admin-con-barra'),



    # Template views (LOGIN)
    path('api/auth/login/', login, name='login'),
    path('api/auth/register/', register, name='register'),
    path('api/auth/bartender/login/', bartender_login, name='bartender-login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Redirect root to login (IA)
    path('', login_view, name='root'),

    #Estimador de líquido
    path('estimate_liquid/', views.EstimateLiquidView.as_view(), name='estimate_liquid'),
]

