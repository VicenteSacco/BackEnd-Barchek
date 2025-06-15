from django.urls import path
from myapp.views import AlcoholListCreate, AlcoholRetrieveUpdateDestroy,alcohol_list,alcohol_create,ReporteListCreate,ReporteRetrieveUpdateDestroy,AdministradorListCreate,AdministradorRetrieveUpdateDestroy,BarraListCreate,BarraRetrieveUpdateDestroy,ListaaalcoholRetrieveUpdateDestroy,ListaaalcoholListCreate,ListaDeAlcoholListCreate,ListaDeAlcoholRetrieveUpdateDestroy,EstimateLiquidView
from myapp import views
from django.contrib import admin
from myapp.views import login_view, register_view, dashboard_view
from rest_framework_simplejwt.views import TokenRefreshView
from myapp.auth import login, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alcohol_list/', views.alcohol_list, name='alcohol_list'),
    path('alcohol/create/', views.alcohol_create, name='alcohol_create'),
    path('alcohol/update/<int:pk>/', views.alcohol_update, name='alcohol_update'),
    path('alcohol/delete/<int:pk>/', views.alcohol_delete, name='alcohol_delete'),

    


    # API Endpoints
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
    # Template views
    path('api/auth/login/', login, name='login'),
    path('api/auth/register/', register, name='register'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Redirect root to login
    path('', login_view, name='root'),
    #Estimador de líquido
    path('estimate_liquid/', EstimateLiquidView.as_view(), name='estimate_liquid'),
]
