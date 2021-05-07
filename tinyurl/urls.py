from django.urls import path
from . import views
from . import short_view
from . import long_view


urlpatterns = [
    path('', views.index),
    path('s/', short_view.short_url),
    path('s/<str:key>', long_view.full_url)
]