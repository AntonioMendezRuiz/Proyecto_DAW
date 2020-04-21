from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PrincipalView, name="home"),
    path('consulta/', views.consulta, name="consulta"),
]
