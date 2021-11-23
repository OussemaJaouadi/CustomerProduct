from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name="home"),
    path('user/',views.userPage,name ="user"),
    path('home/', views.Home,name="home"),
    path('products/',views.Products_view,name="products"),
    path('customer/<int:id>/',views.Customer_view,name="customer"),
    path('order/',views.UOrder,name="order_manage"),
    path('order/<int:order_id>/',views.UOrder,name="order_manage"),
    path('order/delete/<int:id>/',views.DOrder,name="order_delete"),
    path('customer_order/<int:customer_id>/',views.COrder,name="custom_create_order"),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('register/',views.Register,name='register')
]