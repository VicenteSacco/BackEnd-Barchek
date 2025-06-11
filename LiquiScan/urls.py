from django.urls import path
from myapp.views import AlcoholListCreate, AlcoholRetrieveUpdateDestroy,alcohol_list,alcohol_create,SeleccionAlcoholView
from myapp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alcohol_list/', views.alcohol_list, name='alcohol_list'),
    path('alcohol/create/', views.alcohol_create, name='alcohol_create'),
    path('alcohol/update/<int:pk>/', views.alcohol_update, name='alcohol_update'),
    path('alcohol/delete/<int:pk>/', views.alcohol_delete, name='alcohol_delete'),

    # API Endpoints
    path('api/alcohol/', AlcoholListCreate.as_view(), name='alcohol-list-create'),
    path('api/alcohol/<int:pk>/', AlcoholRetrieveUpdateDestroy.as_view(), name='alcohol-detail'),
    path('api/alcohol/<int:pk>/select/', SeleccionAlcoholView.as_view(), name='alcohol-select')
]
