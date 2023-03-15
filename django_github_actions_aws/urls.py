from unirawscp2eb.contrib import admin
from unirawscp2eb.urls import path
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
