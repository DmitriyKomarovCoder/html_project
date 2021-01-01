from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('my-ads', views.myads),
    path('ad', views.ad),
    path("redactor", views.redactor),
    path('reg', views.reg),
    path('enter', views.enter)
]
