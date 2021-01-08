from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('my-ads', views.myads),
    path("redactor", views.redactor),
    path('log', views.LoginFormView.as_view(), name='log'),
    path('reg', views.UserRegisterView.as_view(), name="registration" ),
    path('<int:pk>', views.PAGE_OF_PRODUCT.as_view(), name='ad'),
    path('<int:pk>/update', views.PAGE_OF_UPDATE.as_view(), name='update_ad'),
    path('<int:pk>/delete', views.PAGE_OF_DELETE.as_view(), name='delete_ad'),
    path('logout', views.UserLogout.as_view(), name='logout')

]
