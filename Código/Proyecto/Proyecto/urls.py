from django.contrib import admin
from django.urls import path
from principal.views import PrincipalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PrincipalView.as_view(), name="home"),
]
