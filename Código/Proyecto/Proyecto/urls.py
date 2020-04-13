from django.contrib import admin
from django.urls import path
from principal.views import PrincipalView, RespuestasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PrincipalView.as_view(), name="home"),
    path('consulta/', RespuestasView.as_view(), name="consulta"),
]
