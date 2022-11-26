from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from taalyApp import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
]

#urlpatterns += staticfiles_urlpatterns()